import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Получаем токен из переменных окружения Railway
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    welcome_text = f"Привет, {user.first_name}! 👋\nДобро пожаловать!"
    
    keyboard = [["START"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def handle_actions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "START":
        actions_keyboard = [
            ["📊 Услуги", "📞 Контакты"],
            ["ℹ️ Помощь", "👨‍💻 О проекте"]
        ]
        reply_markup = ReplyKeyboardMarkup(actions_keyboard, resize_keyboard=True)
        await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)
    
    elif text == "📊 Услуги":
        await update.message.reply_text("Наши услуги...")
    
    elif text == "📞 Контакты":
        await update.message.reply_text("Наши контакты...")
    
    elif text == "ℹ️ Помощь":
        await update.message.reply_text("Помощь...")
    
    elif text == "👨‍💻 О проекте":
        await update.message.reply_text("О проекте...")

def main():
    if not BOT_TOKEN:
        logging.error("BOT_TOKEN не установлен!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_actions))
    
    logging.info("🚀 Бот запущен на Railway!")
    application.run_polling()

if __name__ == "__main__":
    main()
