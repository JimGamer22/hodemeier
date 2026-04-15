import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import altair as alt
from datetime import datetime

MAP_MODES = {"1": "venture", "2": "oasis", "3": "slurp rush"}
MAP_COLORS = {"venture": "#e05c3a", "oasis": "#2d9c6e", "slurp rush": "#4a7fc1"}


def calculate_kelly(prob, yes_pct):
    if yes_pct <= 0 or yes_pct >= 100:
        return 0
    odds = 100 / yes_pct
    b = odds - 1
    p = prob / 100
    if b <= 0:
        return 0
    f = (p * (b + 1) - 1) / b
    return max(0, f / 2)


def render_predictor_tab():
    st.markdown("## 📊 ApoRed Predictor")

    conn = st.connection("gsheets", type=GSheetsConnection)


    def load_data():
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            # Nutze die ID direkt aus den Secrets
            df = conn.read(
                spreadsheet=st.secrets["sheets"]["apored_sheet_id"],
                worksheet=st.secrets["sheets"]["apored_worksheet"]
            )
            return df
        except Exception as e:
            st.error(f"Fehler beim Laden: {e}")
            return pd.DataFrame()

    df = load_data()

    # ── Dashboard-Metriken ──────────────────────────────────────────
    total = len(df)
    avg_kills = round(df["kills"].mean(), 1) if total > 0 else 0
    avg_platz = round(df["platz"].mean(), 1) if total > 0 else 0
    win_rate = round((df["win_vorher"].sum() / total * 100), 1) if total > 0 else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Runden gesamt", total)
    c2.metric("Ø Kills", avg_kills)
    c3.metric("Ø Platzierung", avg_platz)
    c4.metric("Win-Rate vorher", f"{win_rate} %")

    st.markdown("---")

    # ── Tabs ────────────────────────────────────────────────────────
    tab1, tab2, tab3, tab4 = st.tabs(["🎯  Wette prüfen", "➕  Runde eintragen", "📈  Statistiken", "🗑  Daten verwalten"])

    with tab1:
        st.markdown("#### Twitch Live-Analyse")
        col_a, col_b = st.columns([1, 1])
        with col_a:
            target = st.number_input("Wette (Kills):", min_value=0, value=10, key="bet_kills")
            m_id = st.selectbox("Map:", options=list(MAP_MODES.keys()), format_func=lambda x: MAP_MODES[x], key="map_select")
            l_win = st.checkbox("Letzte Runde Sieg?", key="last_win")
        with col_b:
            yes_pct = st.slider("JA-Quote (%):", 1, 99, 50, key="yes_slider")
            st.markdown("<br>", unsafe_allow_html=True)
            calc = st.button("Chance berechnen →", key="calc_btn", type="primary", use_container_width=True)

        if calc:
            map_name = MAP_MODES[m_id]
            map_df = df[df["map"] == map_name] if not df.empty else pd.DataFrame()

            if map_df.empty:
                st.info(f"Keine Daten für **{map_name}** vorhanden — bitte erst Runden eintragen.")
            else:
                if len(map_df) < 10:
                    st.warning(f"⚠️ Nur {len(map_df)} Einträge für {map_name} — Schätzung ungenau.")

                prob = (map_df["kills"] >= target).mean() * 100

                # Form-Faktor (letzte 3 Runden)
                if len(df) >= 3:
                    try:
                        form = (df.tail(3)["kills"].mean() - df["kills"].mean()) * 2
                        prob += form
                    except Exception:
                        pass

                # Placement-Bonus: top 10 häufiger → +5 %
                if not map_df.empty:
                    top10_rate = (map_df["platz"] <= 10).mean()
                    prob += (top10_rate - 0.5) * 10

                if l_win:
                    prob -= 10

                prob = max(5, min(95, prob))
                odds = 100 / yes_pct
                ev = (prob / 100) * odds
                kelly = calculate_kelly(prob, yes_pct) * 100

                st.markdown("---")
                r1, r2, r3 = st.columns(3)
                r1.metric("Gewinnchance", f"{prob:.1f} %")
                r2.metric("Expected Value", f"{ev:.2f}x")
                r3.metric("Kelly-Einsatz", f"{kelly:.1f} %")

                if ev > 1.05 and kelly > 0:
                    st.success(f"✅  TIPP: JA — Setze {kelly:.1f} % deines Budgets")
                else:
                    st.error(f"❌  KEIN JA — EV zu niedrig ({ev:.2f}x)")

    with tab2:
        st.markdown("#### Neue Runde eintragen")
        col_x, col_y = st.columns(2)
        with st.form("add_round"):
            fc1, fc2, fc3 = st.columns(3)
            with fc1:
                p = st.number_input("Platzierung", 1, 50, 1)
            with fc2:
                k = st.number_input("Kills", 0, 100, 5)
            with fc3:
                m_add = st.selectbox("Map", options=list(MAP_MODES.keys()), format_func=lambda x: MAP_MODES[x])
            wv = st.checkbox("War es ein Sieg?")
            submitted = st.form_submit_button("💾  In Cloud speichern", use_container_width=True, type="primary")

            if submitted:
                new_row = pd.DataFrame([{
                    "runde": len(df) + 1,
                    "platz": p,
                    "kills": k,
                    "map": MAP_MODES[m_add],
                    "win_vorher": wv,
                    "stunde": datetime.now().hour,
                }])
                updated_df = pd.concat([df, new_row], ignore_index=True)
                try:
                    conn.update(worksheet="stats", data=updated_df)
                    st.success("✅ Gespeichert!")
                    st.cache_data.clear()
                    st.rerun()
                except Exception as e:
                    st.error(f"Fehler: {e}")

    with tab3:
        st.markdown("#### Statistiken")
        if df.empty:
            st.info("Noch keine Daten vorhanden.")
        else:
            col_g1, col_g2 = st.columns(2)

            with col_g1:
                st.markdown("**Kills-Verteilung pro Map**")
                chart_box = alt.Chart(df).mark_boxplot(extent="min-max").encode(
                    x=alt.X("map:N", title="Map"),
                    y=alt.Y("kills:Q", title="Kills"),
                    color=alt.Color("map:N", legend=None),
                ).properties(height=240)
                st.altair_chart(chart_box, use_container_width=True)

            with col_g2:
                st.markdown("**Kills über Zeit**")
                chart_line = alt.Chart(df).mark_line(point=True).encode(
                    x=alt.X("runde:Q", title="Runde"),
                    y=alt.Y("kills:Q", title="Kills"),
                    color=alt.Color("map:N"),
                    tooltip=["runde", "kills", "platz", "map"],
                ).properties(height=240)
                st.altair_chart(chart_line, use_container_width=True)

            st.markdown("**Letzte 15 Runden**")
            st.dataframe(
                df.sort_values("runde", ascending=False).head(15),
                use_container_width=True,
                hide_index=True,
            )

    with tab4:
        st.markdown("#### Daten korrigieren")
        if df.empty:
            st.info("Keine Daten vorhanden.")
        else:
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                runde_to_delete = st.selectbox("Runde löschen:", options=df["runde"].tolist())
                if st.button("🗑  Ausgewählte Runde löschen", type="primary"):
                    updated_df = df[df["runde"] != runde_to_delete].reset_index(drop=True)
                    updated_df["runde"] = range(1, len(updated_df) + 1)
                    try:
                        conn.update(worksheet="stats", data=updated_df)
                        st.success(f"Runde {runde_to_delete} gelöscht.")
                        st.cache_data.clear()
                        st.rerun()
                    except Exception as e:
                        st.error(f"Fehler: {e}")

            with col_d2:
                st.markdown("**Letzte Zeile löschen**")
                if st.button("🗑  Letzte Zeile löschen"):
                    updated_df = df.iloc[:-1]
                    try:
                        conn.update(worksheet="stats", data=updated_df)
                        st.success("Letzte Zeile gelöscht.")
                        st.cache_data.clear()
                        st.rerun()
                    except Exception as e:
                        st.error(f"Fehler: {e}")
