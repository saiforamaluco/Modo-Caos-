import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def modocaos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type not in ["group", "supergroup"]:
        return

    if not context.args:
        return

    mensagem = " ".join(context.args)

    try:
        await update.message.delete()
    except:
        pass

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"🔥 MODO CAOS ATIVADO\n\n💣 {mensagem}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("modocaos", modocaos))

PORT = int(os.environ.get("PORT", 10000))

app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=f"https://SEU-NOME-DO-APP.onrender.com/{TOKEN}"
)
