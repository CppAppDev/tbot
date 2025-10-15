import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    welcome_text = f"""Привет, {user.first_name}! 👋

Добро пожаловать в наш сервисный бот!
Здесь вы можете узнать о наших услугах и связаться с нами."""

    # Клавиатура с кнопками под приветствием
    keyboard = [
        ["🎯 Услуги", "📞 Контакты"],
        ["ℹ️ О нас", "🆘 Помощь"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def handle_actions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "🎯 Услуги":
        services_text = """Наши услуги:

• 🤖 Разработка Telegram ботов
• 🌐 Создание веб-сайтов
• 📱 Мобильные приложения
• 🔧 Техническая поддержка
• 💼 Консультации

Выберите интересующую услугу для подробностей:"""

        services_keyboard = [
            ["🤖 Боты", "🌐 Сайты"],
            ["📱 Приложения", "🔧 Поддержка"],
            ["⬅️ Назад"]
        ]
        reply_markup = ReplyKeyboardMarkup(services_keyboard, resize_keyboard=True)
        await update.message.reply_text(services_text, reply_markup=reply_markup)
    
    elif text == "📞 Контакты":
        await update.message.reply_text(
            "📞 Наши контакты:\n\n"
            "📧 Email: example@mail.ru\n"
            "📱 Телефон: +7 XXX XXX-XX-XX\n"
            "🌐 Сайт: example.com"
        )
    
    elif text == "ℹ️ О нас":
        await update.message.reply_text(
            "👨‍💻 О нашей компании:\n\n"
            "Мы занимаемся разработкой IT-решений\n"
            "Более 5 лет на рынке\n"
            "50+ успешных проектов"
        )
    
    elif text == "🆘 Помощь":
        await update.message.reply_text(
            "❓ Помощь по боту:\n\n"
            "• Выберите 'Услуги' для просмотра предложений\n"
            "• 'Контакты' - для связи с нами\n"
            "• 'О нас' - информация о компании\n\n"
            "Для возврата в главное меню используйте кнопку 'Назад'"
        )
    
    elif text == "⬅️ Назад":
        # Возврат в главное меню
        keyboard = [
            ["🎯 Услуги", "📞 Контакты"],
            ["ℹ️ О нас", "🆘 Помощь"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Главное меню:", reply_markup=reply_markup)
    
    elif text in ["🤖 Боты", "🌐 Сайты", "📱 Приложения", "🔧 Поддержка"]:
        service_details = {
            "🤖 Боты": "Разработка Telegram ботов любой сложности:\n• Автоматизация\n• Интеграции с API\n• Боты для бизнеса",
            "🌐 Сайты": "Создание современных веб-сайтов:\n• Landing pages\n• Интернет-магазины\n• Корпоративные сайты",
            "📱 Приложения": "Разработка мобильных приложений:\n• iOS и Android\n• Кроссплатформенные решения",
            "🔧 Поддержка": "Техническая поддержка:\n• Исправление ошибок\n• Обновление функционала\n• Консультации"
        }
        
        detail_text = service_details.get(text, "Информация об услуге")
        detail_keyboard = [["⬅️ Назад к услугам"]]
        reply_markup = ReplyKeyboardMarkup(detail_keyboard, resize_keyboard=True)
        await update.message.reply_text(detail_text, reply_markup=reply_markup)
    
    elif text == "⬅️ Назад к услугам":
        await handle_actions(update, context)  # Возврат к услугам

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
