import string
import cgi

def toHTML(str):
	str = cgi.escape(str)
	bs = 20
	ea = 21
	bold = 22
	ital = 23
	str = string.replace(str, "\\\\", chr(bs))
	str = string.replace(str, "\*", chr(ea))
	str = string.replace(str, "**", chr(bold))
	str = string.replace(str, "*", chr(ital))
	i = 0
	consecAst = 0
	depth = 0
	while i < len(str):
		v = str[i]
		if v == chr(ital):
			if depth == 1:
				str = string.replace(str, chr(ital), "</i>", 1)
				depth -= 1
			else:
				str = string.replace(str, chr(ital), "<i>", 1)
				depth += 1
		elif v == chr(bold):
			if depth == 1:
				str = string.replace(str, chr(bold), "</b>", 1)
				depth -= 1
			else:
				str = string.replace(str, chr(bold), "<b>", 1)
				depth += 1
		i += 1
	str = string.replace(str, chr(bs), "\\")
	str = string.replace(str, chr(ea), "*")
	return str
