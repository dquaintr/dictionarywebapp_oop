import justpy as jp
from design.webapp.homepage import Home
from design.webapp.aboutpage import About
from design.webapp.dictionary import Dictionary

jp.Route(Dictionary.path, Dictionary.serve)
jp.Rout(Home.path, Home.serve)
jp.Route(About.path, About.serve)


jp.justpy(Port=8001)
