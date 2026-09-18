import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import google.generativeai as genai

# Setup logging
logging.basicConfig(
 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
 level=logging.INFO
)

# Configure Gemini API
genai.configure(api_key="AQ.Ab8RN6JOPW1gohQ85T18MUnqYz1Rpz8IM8Tc_sgcFw4yDfK_Ag")
model = genai.GenerativeModel('gemini-1.5-flash')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
 user_message = update.message.text
 response = model.generate_content(user_message)
 await context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)

if __name__ == '__main__':
 application = ApplicationBuilder().token('8863800334:AAEv_k_3v8Ka12YnCgLMLpHog1MqaTdNMAA').build()
 message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
 application.add_handler(message_handler)

 application.run_polling()
