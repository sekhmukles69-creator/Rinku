from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import google.generativeai as genai

genai.configure(api_key='AQ.Ab8RN6JOPW1gohQ85T18MUnqYz1Rpz8IM8Tc_sgcFw4yDfK_Ag')
model = genai.GenerativeModel('gemini-pro')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your Telegram Bot, powered by Gemini AI.')

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = model.generate_content(user_message)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text('Sorry, there was an error.')

if __name__ == '__main__':
    application = ApplicationBuilder().token('8863800334:AAEv_k_3v8Ka12YnCgLMLpHog1MqaTdNMAA').build()
    
    start_handler = CommandHandler('start', start)
    chat_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), chat)
    
    application.add_handler(start_handler)
    application.add_handler(chat_handler)
    
    application.run_polling()
 
