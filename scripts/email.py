import smtplib
import logging
from email.message import EmailMessage
from email.utils import formatdate
import os
from dotenv import load_dotenv
import ssl

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def send_etl_notification(status: str, error_message: str = None) -> None:
    """
    Sends an ETL process notification email
    
    :param status: 'success' or 'failure'
    :param error_message: Detailed error message (required for failures)
    """
    # Validate inputs
    if status not in ['success', 'failure']:
        raise ValueError("Status must be 'success' or 'failure'")
    
    if status == 'failure' and not error_message:
        raise ValueError("Error message is required for failure notifications")

    # Configure email parameters
    subject = f"ETL Process {'✅ Completed Successfully' if status == 'success' else '❌ Failed'}"
    sender = os.getenv("EMAIL_SENDER")
    receiver = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")
    
    # Create email content
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg['Date'] = formatdate(localtime=True)
    
    if status == 'success':
        content = """
        The ETL process completed successfully.
        
        Details:
        - Cleaned data loaded into PostgreSQL
        - All transformations executed as expected
        """
    else:
        content = f"""
        The ETL process encountered an error!
        
        Error Details:
        {error_message}
        
        Action Required:
        - Check system logs
        - Verify data sources
        - Review processing pipeline
        """
    
    msg.set_content(content.strip())

    # Send email with secure connection
    try:
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender, password)
            server.send_message(msg)
            logger.info(f"ETL {status} notification sent to {receiver}")
            
    except smtplib.SMTPAuthenticationError:
        logger.error("Authentication failed - check email credentials")
    except smtplib.SMTPException as e:
        logger.error(f"SMTP protocol error: {str(e)}")
    except Exception as e:
        logger.exception(f"Unexpected error sending email: {str(e)}")


