package lang

//messages has the static messages for validations, groupped by language
var messages = languageList{
	"en": map[string]string{
		"ticketsNameRequired": "The user name is required",
		"genericFail":         "Something was wrong!",
	},
	"es": map[string]string{
		"ticketsNameRequired": "El nombre del condenado es requerido",
		"genericFail":         "falio ferga!",
	},
}
