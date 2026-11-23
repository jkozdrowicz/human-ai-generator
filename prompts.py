SENTENCE_VARIABILITY = {
    1: "Buduj zdania o bardzo podobnej długości. Unikaj bardzo krótkich i bardzo długich zdań.",
    2: "Utrzymuj raczej podobną długość zdań, dopuszczając niewielkie różnice.",
    3: "Stosuj umiarkowane zróżnicowanie długości zdań.",
    4: "Wyraźnie różnicuj długość zdań, łącząc krótsze i dłuższe konstrukcje.",
    5: "Stosuj bardzo duże zróżnicowanie długości zdań. Łącz bardzo krótkie zdania z długimi i rozbudowanymi."
}

STRUCTURE_REGULARITY = {
    1: "Stosuj bardzo regularną i przewidywalną strukturę tekstu oraz podobne schematy budowania kolejnych zdań i akapitów.",
    2: "Zachowaj dość regularną i uporządkowaną strukturę.",
    3: "Zachowaj spójną strukturę, ale nie przesadzaj z jej regularnością.",
    4: "Różnicuj konstrukcje zdań i sposób organizacji kolejnych fragmentów tekstu.",
    5: "Unikaj powtarzalnych schematów. Struktura powinna być spójna, ale swobodna i mało przewidywalna."
}

LANGUAGE_SMOOTHNESS = {
    1: "Pisz bardzo starannie, poprawnie i jednolicie. Dbaj o płynne przejścia i konsekwentny styl.",
    2: "Pisz językiem wyraźnie uporządkowanym i stylistycznie wygładzonym.",
    3: "Pisz poprawnym i naturalnym językiem, bez nadmiernego wygładzania stylu.",
    4: "Dopuszczaj drobne nierówności stylistyczne i mniej idealne przejścia między myślami.",
    5: "Pisz naturalnie i mniej jednolicie stylistycznie. Dopuszczaj niewielkie nierówności w sposobie formułowania myśli, ale nie wprowadzaj celowo rażących błędów."
}

TONE_PROFILE = {
    1: "Utrzymuj bardzo neutralny, zdystansowany i obiektywizujący ton. Unikaj osobistych ocen i emocjonalnych sformułowań.",
    2: "Utrzymuj głównie neutralny i zdystansowany ton.",
    3: "Zachowaj neutralny ton, ale dopuszczaj pojedyncze elementy oceniające lub bardziej osobiste.",
    4: "Dopuszczaj więcej subiektywnych ocen, zastrzeżeń i emocjonalnych sformułowań.",
    5: "Nadaj tekstowi bardziej osobisty i subiektywny charakter. Dopuszczaj wyraźniejsze oceny, emocje i indywidualny sposób przedstawiania informacji."
}


def build_prompt(
    topic,
    text_length,
    sentence_variability,
    structure_regularity,
    language_smoothness,
    tone_profile
):
    prompt = f"""
Napisz tekst w języku polskim.

Temat: {topic}
Docelowa długość: około {text_length} słów.

Zastosuj następujące zasady:

1. Zmienność długości zdań:
{SENTENCE_VARIABILITY[sentence_variability]}

2. Regularność struktury:
{STRUCTURE_REGULARITY[structure_regularity]}

3. Wygładzenie języka:
{LANGUAGE_SMOOTHNESS[language_smoothness]}

4. Ton wypowiedzi:
{TONE_PROFILE[tone_profile]}

Nie komentuj zastosowanych ustawień.
Nie informuj, że tekst został wygenerowany.
Zwróć wyłącznie gotowy tekst.
"""

    return prompt.strip()