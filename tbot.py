import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    
    welcome_text = f"""🌟 <b>Добро пожаловать, {user.first_name}!</b> 🌟

Я ваш помощник в мире IT-услуг. 
Выберите, что вас интересует, и мы сразу перейдем к нужному разделу:"""

    # Инлайн-кнопки с переходами
    keyboard = [
        [InlineKeyboardButton("🚀 Наши услуги", callback_data="services")],
        [InlineKeyboardButton("📞 Связаться с нами", callback_data="contacts")],
        [InlineKeyboardButton("💼 Портфолио", callback_data="portfolio")],
        [InlineKeyboardButton("❓ Частые вопросы", callback_data="faq")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='HTML')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "services":
        services_text = """<b>🎯 Наши IT-услуги:</b>

• 🤖 <b>Telegram боты</b> - автоматизация бизнеса
• 🌐 <b>Веб-разработка</b> - сайты и веб-приложения  
• 📱 <b>Мобильные приложения</b> - iOS и Android
• 🛠 <b>Техническая поддержка</b> - сопровождение проектов
• 💡 <b>Консультации</b> - IT-аудит и стратегия"""

        services_keyboard = [
            [InlineKeyboardButton("🤖 Узнать о ботах", callback_data="bot_details")],
            [InlineKeyboardButton("🌐 Веб-разработка", callback_data="web_details")],
            [InlineKeyboardButton("📱 Приложения", callback_data="app_details")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
        ]
        reply_markup = InlineKeyboardMarkup(services_keyboard)
        await query.edit_message_text(services_text, reply_markup=reply_markup, parse_mode='HTML')
    
    elif data == "contacts":
        contacts_text = """<b>📞 Контакты для связи:</b>

💌 <b>Email:</b> hello@company.ru
📱 <b>Telegram:</b> @manager_name
🌐 <b>Сайт:</b> company.ru
📍 <b>Время работы:</b> Пн-Пт 9:00-18:00

<b>Напишите нам — обсудим ваш проект!</b>"""
        
        contacts_keyboard = [
            [InlineKeyboardButton("💌 Написать на email", url="mailto:hello@company.ru")],
            [InlineKeyboardButton("📱 Написать в Telegram", url="https://t.me/manager_name")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
        ]
        reply_markup = InlineKeyboardMarkup(contacts_keyboard)
        await query.edit_message_text(contacts_text, reply_markup=reply_markup, parse_mode='HTML')
    
    elif data == "portfolio":
        portfolio_text = """<b>💼 Наше портфолио:</b>

📊 <b>Более 50 успешных проектов</b>

🎯 <b>Примеры работ:</b>
• E-commerce бот с оплатой - <b>+300%</b> к конверсии
• Мобильное приложение - <b>50k+</b> установок
• Корпоративный портал - автоматизация для <b>200+</b> сотрудников"""

        portfolio_keyboard = [
            [InlineKeyboardButton("📊 Посмотреть кейсы", callback_data="cases")],
            [InlineKeyboardButton("💬 Отзывы клиентов", callback_data="reviews")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
        ]
        reply_markup = InlineKeyboardMarkup(portfolio_keyboard)
        await query.edit_message_text(portfolio_text, reply_markup=reply_markup, parse_mode='HTML')
    
    elif data == "faq":
        faq_text = """<b>❓ Частые вопросы:</b>

<b>Q:</b> Сколько времени занимает разработка?
<b>A:</b> От 2 недель до 3 месяцев в зависимости от сложности

<b>Q:</b> Какие технологии используете?
<b>A:</b> Python, JavaScript, React, Node.js, PostgreSQL

<b>Q:</b> Предоставляете ли техподдержку?
<b>A:</b> Да, от 1 месяца до 1 года после запуска"""

        faq_keyboard = [
            [InlineKeyboardButton("💬 Задать свой вопрос", callback_data="ask_question")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main")]
        ]
        reply_markup = InlineKeyboardMarkup(faq_keyboard)
        await query.edit_message_text(faq_text, reply_markup=reply_markup, parse_mode='HTML')
    
    elif data == "back_to_main":
        # Возврат к главному меню
        await start(update, context)

async def handle_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "bot_details":
        text = """<b>🤖 Разработка Telegram ботов:</b>

🎯 <b>Что мы делаем:</b>
• Боты для автоматизации бизнеса
• Чат-боты с AI
• Боты для e-commerce
• Интеграции с CRM и API

💰 <b>Стоимость:</b> от 15 000 ₽
⏱ <b>Сроки:</b> от 2 недель"""

    elif data == "web_details":
        text = """<b>🌐 Веб-разработка:</b>

🎯 <b>Что мы делаем:</b>
• Landing pages
• Интернет-магазины
• Корпоративные сайты
• Веб-приложения

💰 <b>Стоимость:</b> от 25 000 ₽
⏱ <b>Сроки:</b> от 3 недель"""

    keyboard = [
        [InlineKeyboardButton("💬 Обсудить проект", callback_data="contacts")],
        [InlineKeyboardButton("⬅️ Назад к услугам", callback_data="services")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='HTML')

def main():
    if not BOT_TOKEN:
        logging.error("BOT_TOKEN не установлен!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler, pattern="^(services|contacts|portfolio|faq|back_to_main|cases|reviews|ask_question)$"))
    application.add_handler(CallbackQueryHandler(handle_details, pattern="^(bot_details|web_details|app_details)$"))
    
    logging.info("🚀 Бот с инлайн-кнопками запущен!")
    application.run_polling()

if __name__ == "__main__":
    main()
