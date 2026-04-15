import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
import uuid

# Email Templates
EMAIL_TEMPLATES = {
    "welcome": {
        "name": "🎉 Willkommen",
        "subject": "Willkommen bei {company}!",
        "body": """Hallo {recipient_name},

herzlich willkommen in unserem Team!

Wir freuen uns auf die Zusammenarbeit mit dir.

Viele Grüße,
Das Team"""
    },
    "notification": {
        "name": "🔔 Benachrichtigung",
        "subject": "Wichtige Benachrichtigung: {title}",
        "body": """Hallo {recipient_name},

hier ist eine wichtige Benachrichtigung für dich:

{message}

Weitere Informationen findest du im Dashboard.

Viele Grüße,
Das Team"""
    },
    "reminder": {
        "name": "⏰ Erinnerung",
        "subject": "Erinnerung: {title}",
        "body": """Hallo {recipient_name},

dies ist eine freundliche Erinnerung für dich:

{message}

Bitte handle bis zum {deadline}.

Viele Grüße,
Das Team"""
    },
    "report": {
        "name": "📊 Bericht",
        "subject": "Monatlicher Bericht: {month}",
        "body": """Hallo {recipient_name},

anbei findest du deinen Monatsbericht für {month}:

{message}

Weitere Metriken sind im Dashboard verfügbar.

Viele Grüße,
Das Team"""
    },
    "custom": {
        "name": "✍️ Benutzerdefiniert",
        "subject": "",
        "body": ""
    }
}


def generate_email_id():
    """Generiert eine eindeutige Email-ID"""
    return str(uuid.uuid4())[:8]


def render_email_generator_tab():
    st.markdown("## 📧 Email Generator")
    
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    def load_emails():
        try:
            data = conn.read(worksheet="emails", ttl=0)
            if data is None or data.empty:
                return pd.DataFrame(columns=[
                    "email_id", "sender", "recipient", "recipient_name", "subject", 
                    "body", "template", "status", "created_at", "sent_at"
                ])
            return data
        except Exception:
            return pd.DataFrame(columns=[
                "email_id", "sender", "recipient", "recipient_name", "subject", 
                "body", "template", "status", "created_at", "sent_at"
            ])
    
    emails_df = load_emails()
    
    # ── Dashboard-Metriken ──────────────────────────────────────────
    total_emails = len(emails_df)
    sent_count = len(emails_df[emails_df["status"] == "gesendet"]) if not emails_df.empty else 0
    draft_count = len(emails_df[emails_df["status"] == "Entwurf"]) if not emails_df.empty else 0
    scheduled_count = len(emails_df[emails_df["status"] == "geplant"]) if not emails_df.empty else 0
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Gesamt Emails", total_emails)
    c2.metric("Gesendet", sent_count, delta=None)
    c3.metric("Entwürfe", draft_count)
    c4.metric("Geplant", scheduled_count)
    
    st.markdown("---")
    
    # ── Tabs ────────────────────────────────────────────────────────
    tab1, tab2, tab3 = st.tabs(["✉️  Email erstellen", "📋  Dashboard", "🗑  Verwalten"])
    
    with tab1:
        st.markdown("#### Neue Email generieren")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            sender_name = st.text_input("Absendername", value="Hodemeier Team", key="sender_name")
            sender_email = st.text_input("Absender Email", value="noreply@hodemeier.de", key="sender_email")
            recipient_email = st.text_input("Empfänger Email", placeholder="user@example.com", key="recipient_email")
            recipient_name = st.text_input("Empfänger Name", placeholder="Max Mustermann", key="recipient_name")
        
        with col_b:
            template_choice = st.selectbox(
                "Template auswählen",
                options=list(EMAIL_TEMPLATES.keys()),
                format_func=lambda x: EMAIL_TEMPLATES[x]["name"],
                key="template_select"
            )
            
            email_status = st.selectbox(
                "Status",
                options=["Entwurf", "geplant", "gesendet"],
                key="email_status"
            )
            
            company_name = st.text_input("Unternehmensname (optional)", value="Hodemeier", key="company_name")
        
        # Template-Felder
        st.markdown("---")
        st.markdown("#### Email-Inhalt")
        
        template = EMAIL_TEMPLATES[template_choice]
        
        subject = st.text_input(
            "Betreff",
            value=template["subject"],
            key="subject_input"
        )
        
        body = st.text_area(
            "Nachricht",
            value=template["body"],
            height=250,
            key="body_input"
        )
        
        # Template-Variablen ersetzen
        st.markdown("**Verfügbare Variablen:**")
        st.caption("Use `{company}`, `{recipient_name}`, `{title}`, `{message}`, `{deadline}`, `{month}`")
        
        if st.button("✉️  Email-Vorschau", key="preview_btn", use_container_width=True):
            preview_subject = subject.format(
                company=company_name,
                recipient_name=recipient_name or "Empfänger",
                title="[Titel]",
                month="[Monat]"
            ) if "{" in subject else subject
            
            preview_body = body.format(
                company=company_name,
                recipient_name=recipient_name or "Empfänger",
                title="[Titel]",
                message="[Nachricht]",
                deadline="[Datum]",
                month="[Monat]"
            ) if "{" in body else body
            
            st.info(f"**Betreff:** {preview_subject}\n\n{preview_body}")
        
        st.markdown("---")
        
        if st.button("💾  Email speichern", key="save_btn", type="primary", use_container_width=True):
            if not recipient_email or not subject:
                st.error("Bitte Empfänger Email und Betreff ausfüllen.")
            else:
                new_email = pd.DataFrame([{
                    "email_id": generate_email_id(),
                    "sender": f"{sender_name} <{sender_email}>",
                    "recipient": recipient_email,
                    "recipient_name": recipient_name or recipient_email,
                    "subject": subject,
                    "body": body,
                    "template": EMAIL_TEMPLATES[template_choice]["name"],
                    "status": email_status,
                    "created_at": datetime.now().strftime("%d.%m.%Y %H:%M"),
                    "sent_at": "" if email_status != "gesendet" else datetime.now().strftime("%d.%m.%Y %H:%M"),
                }])
                
                updated_df = pd.concat([emails_df, new_email], ignore_index=True)
                
                try:
                    conn.update(worksheet="emails", data=updated_df)
                    st.success(f"✅ Email an {recipient_email} gespeichert!")
                    st.cache_data.clear()
                    st.rerun()
                except Exception as e:
                    st.error(f"Fehler beim Speichern: {e}")
    
    with tab2:
        st.markdown("#### Email Dashboard")
        
        if emails_df.empty:
            st.info("📭 Noch keine Emails generiert.")
        else:
            # Filter
            col_f1, col_f2, col_f3 = st.columns(3)
            
            with col_f1:
                status_filter = st.multiselect(
                    "Nach Status filtern",
                    options=emails_df["status"].unique().tolist() if "status" in emails_df.columns else [],
                    default=emails_df["status"].unique().tolist() if "status" in emails_df.columns else [],
                    key="status_filter"
                )
            
            with col_f2:
                template_filter = st.multiselect(
                    "Nach Template filtern",
                    options=emails_df["template"].unique().tolist() if "template" in emails_df.columns else [],
                    default=emails_df["template"].unique().tolist() if "template" in emails_df.columns else [],
                    key="template_filter"
                )
            
            with col_f3:
                search_term = st.text_input("🔍 Nach Email/Name durchsuchen", key="search_term")
            
            # Filtering
            filtered_df = emails_df.copy()
            
            if status_filter:
                filtered_df = filtered_df[filtered_df["status"].isin(status_filter)]
            
            if template_filter:
                filtered_df = filtered_df[filtered_df["template"].isin(template_filter)]
            
            if search_term:
                filtered_df = filtered_df[
                    filtered_df["recipient"].str.contains(search_term, case=False, na=False) |
                    filtered_df["recipient_name"].str.contains(search_term, case=False, na=False)
                ]
            
            st.markdown(f"**{len(filtered_df)} Email(s) gefunden**")
            
            # Tabelle mit erweiterten Details
            if not filtered_df.empty:
                display_df = filtered_df.copy()
                display_df = display_df.sort_values("created_at", ascending=False).reset_index(drop=True)
                
                # Formatierte Spalten
                display_df["📧 Empfänger"] = display_df["recipient_name"] + " (" + display_df["recipient"] + ")"
                display_df["📤 Status"] = display_df["status"].apply(
                    lambda x: "✅ Gesendet" if x == "gesendet" else 
                              "📝 Entwurf" if x == "Entwurf" else 
                              "⏱️  Geplant"
                )
                
                show_cols = ["email_id", "📧 Empfänger", "subject", "template", "📤 Status", "created_at"]
                st.dataframe(
                    display_df[show_cols],
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "email_id": st.column_config.TextColumn("ID", width=80),
                        "subject": st.column_config.TextColumn("Betreff", width=300),
                        "template": st.column_config.TextColumn("Template", width=120),
                        "created_at": st.column_config.TextColumn("Erstellt", width=150),
                    }
                )
                
                # Detailansicht
                st.markdown("---")
                st.markdown("#### Email-Details")
                
                selected_id = st.selectbox(
                    "Email auswählen für Detailansicht",
                    options=filtered_df["email_id"].tolist(),
                    format_func=lambda x: f"{x} - {filtered_df[filtered_df['email_id']==x]['recipient'].values[0]}",
                    key="detail_select"
                )
                
                if selected_id:
                    email_detail = filtered_df[filtered_df["email_id"] == selected_id].iloc[0]
                    
                    col_d1, col_d2 = st.columns(2)
                    
                    with col_d1:
                        st.markdown("**Absender**")
                        st.caption(email_detail["sender"])
                        st.markdown("**Empfänger**")
                        st.caption(f"{email_detail['recipient_name']} ({email_detail['recipient']})")
                    
                    with col_d2:
                        st.markdown("**Template**")
                        st.caption(email_detail["template"])
                        st.markdown("**Status**")
                        status_badge = ("✅ Gesendet" if email_detail["status"] == "gesendet" else 
                                       "📝 Entwurf" if email_detail["status"] == "Entwurf" else 
                                       "⏱️  Geplant")
                        st.caption(status_badge)
                    
                    st.markdown("**Betreff**")
                    st.text(email_detail["subject"])
                    
                    st.markdown("**Nachricht**")
                    st.text_area("", value=email_detail["body"], disabled=True, height=200, key="body_display")
                    
                    col_t1, col_t2 = st.columns(2)
                    with col_t1:
                        st.markdown("**Erstellt am**")
                        st.caption(email_detail["created_at"])
                    with col_t2:
                        st.markdown("**Gesendet am**")
                        st.caption(email_detail["sent_at"] if email_detail["sent_at"] else "—")
    
    with tab3:
        st.markdown("#### Email verwalten")
        
        if emails_df.empty:
            st.info("Keine Emails vorhanden.")
        else:
            col_m1, col_m2 = st.columns(2)
            
            with col_m1:
                st.markdown("**Email löschen**")
                email_to_delete = st.selectbox(
                    "Email auswählen",
                    options=emails_df["email_id"].tolist(),
                    format_func=lambda x: f"{x} - {emails_df[emails_df['email_id']==x]['recipient'].values[0]}",
                    key="delete_select"
                )
                
                if st.button("🗑  Löschen", type="primary", use_container_width=True):
                    updated_df = emails_df[emails_df["email_id"] != email_to_delete]
                    try:
                        conn.update(worksheet="emails", data=updated_df)
                        st.success("✅ Email gelöscht.")
                        st.cache_data.clear()
                        st.rerun()
                    except Exception as e:
                        st.error(f"Fehler: {e}")
            
            with col_m2:
                st.markdown("**Alle Emails löschen**")
                st.warning("⚠️ Dies löscht ALLE Emails!")
                if st.button("🗑  Alle löschen", use_container_width=True):
                    try:
                        conn.update(worksheet="emails", data=pd.DataFrame(columns=[
                            "email_id", "sender", "recipient", "recipient_name", "subject", 
                            "body", "template", "status", "created_at", "sent_at"
                        ]))
                        st.success("✅ Alle Emails gelöscht.")
                        st.cache_data.clear()
                        st.rerun()
                    except Exception as e:
                        st.error(f"Fehler: {e}")
