from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_invite_email(recipients, redoc_link, firestore_screenshot_url, github_link):
    from app import app

    message = Mail(
        from_email="",
        to_emails=recipients,
        subject="API Invitation",
        html_content=f"""
        <p>Hello Team,</p>
        <p>Please find the link to the API documentation (ReDoc): <a href="{redoc_link}">{redoc_link}</a></p>
        <p>Here’s a screenshot of the Firestore database: <a href="{firestore_screenshot_url}">Firestore Screenshot</a></p>
        <p>GitHub Code: <a href="{github_link}">{github_link}</a></p>
        <p>Best Regards,</p>
        """,
    )

    try:
        sg = SendGridAPIClient(api_key=app.config.SEND_GRID_API_KEY)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        return str(e)
