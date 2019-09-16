package core

import (
	"github.com/kyokomi/emoji"
	log "github.com/sirupsen/logrus"
	m "github.com/tecnologer/HellOrHeavenBot/model"
	bot "github.com/yanzay/tbot"
)

//SendResponse is in charge of send the data of the response (text, sticker, gif, etc)
func SendResponse(msg *bot.Message, res *m.Response) {
	switch res.Type {
	case m.Text:
		sendText(msg, res.Content)
	case m.Sticker:
		sendSticker(msg, res.Content)
	case m.Gif:
		sendGif(msg, res.Content)
	}
}

func sendText(msg *bot.Message, text string) {
	text = emoji.Sprint(text)
	_, err := Client.SendMessage(msg.Chat.ID, text, bot.OptParseModeMarkdown)
	if err != nil {
		log.WithError(err).WithField("text", text).Error("error when try send text")
	}
}

func sendSticker(msg *bot.Message, stickerID string) {
	_, err := Client.SendSticker(msg.Chat.ID, stickerID)
	if err != nil {
		log.WithError(err).WithField("stickerID", stickerID).Error("error when try send sticker")
	}
}

func sendGif(msg *bot.Message, gifID string) {
	_, err := Client.SendDocument(msg.Chat.ID, gifID)
	if err != nil {
		log.WithError(err).WithField("gifId", gifID).Error("error when try send gif")
	}
}
