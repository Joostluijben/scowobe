"""Generate the static public pages under src. Run with python3 site/build.py."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'src'
ORIGINAL = 'https://scowo.nl'
LOGO = ORIGINAL + '/wp-content/uploads/2026/10/img_logo_white.png'
POSTER = ORIGINAL + '/wp-content/uploads/2026/11/95588a45-574c-4adc-9eda-54df75aabee1-724x1024.jpeg'
SIGNUP = 'https://docs.google.com/forms/d/e/1FAIpQLScB-N_XImGP6tSdF8jARrsekSU1u0nU3UhCjM9wiMmFgI1F8Q/viewform'
CANCEL = 'https://docs.google.com/forms/d/e/1FAIpQLSdRNOW3m4IoMO_q9Bpl1NMPOkm_CcX3FyrHHo_nxwdiF6xMyQ/viewform'
TOUR = 'https://drive.google.com/file/d/1OaUBG5zPIYkwe6sYZBt8Hb-l61ZpjBTZ/view'
ADDRESS = 'https://www.google.com/maps/search/?api=1&query=Kromwijkerdijk+116+Woerden'

MEMBERSHIP = [
    ('Over scouting', '/lidmaatschap/scouting/'),
    ('Speltakken', '/lidmaatschap/speltakken/'),
    ('Aanmelden voor plaatsing', '/lidmaatschap/aanmelden-voor-plaatsing/'),
    ('Lidmaatschap afmelden', '/lidmaatschap/afmelding-voor-lidmaatschap/'),
]
GENERAL = [
    ('NVDKO', ORIGINAL + '/algemeen/nvdko/'),
    ('Stamcafé', ORIGINAL + '/algemeen/stamcafe/'),
    ('Foto’s', 'https://foto.scowo.nl/'),
    ('Geschiedenis', 'https://geschiedenis.scowo.nl/'),
    ('Privacyverklaring', ORIGINAL + '/beleid/privacyverklaring/'),
    ('Sociale veiligheid', ORIGINAL + '/beleid/sociale-veiligheid/'),
    ('Rook- en alcoholbeleid', ORIGINAL + '/beleid/rook-alcoholbeleid/'),
]

NEWS = [
    ('12 nov 2026', '2026-11-12', 'Goededoelenboom te koop!',
     'Bestel je kerstboom bij Scouting Woerden en steun de Buurt Take Away en onze scoutinggroep.',
     '/2026/goededoelenboom-te-koop/'),
    ('27 jun 2026', '2026-06-27', 'Een lokaal doel voor de Goededoelenboom',
     'Scouting Woerden vroeg inwoners een maatschappelijk initiatief aan te dragen voor de opbrengst van de kerstbomenactie.',
     '/2026/goededoelenboom-zoekt-lokaal-goed-doel-voor-editie-2026/'),
    ('9 jun 2026', '2026-06-09', '60 jaar Scouting Woerden',
     'In september kwamen leden en oud-leden samen voor de jubileumreünie van de Albert Schweitzergroep.',
     '/2026/kom-26-september-2026-reuneren/'),
    ('7 jun 2026', '2026-06-07', 'Havendagen Woerden',
     'Een terugblik op Scouting Woerden tijdens de Havendagen.',
     '/2026/havendagen-woerden-2026/'),
    ('19 apr 2026', '2026-04-19', 'Vossenjacht in de binnenstad',
     'Op paaszaterdag zochten honderden deelnemers naar vermomde vossen in Woerden.',
     '/2026/vossenjacht-4-april-2026/'),
    ('29 mrt 2026', '2026-03-29', 'ScowOpen',
     'De jaarlijkse open dag stond in het teken van spelen, proberen en kennismaken met de speltakken.',
     '/2026/activiteiten-en-een-voedselplein-vol-lekkernijen-tijdens-scowopen/'),
]


def link(label, url, css=''):
    style = f' class="{escape(css, quote=True)}"' if css else ''
    return f'<a href="{escape(url, quote=True)}"{style}>{escape(label)}</a>'


def links(items):
    return ''.join(f'<li>{link(label, url)}</li>' for label, url in items)


def nav_link(label, url, active):
    current = ' aria-current="page"' if active else ''
    return f'<a class="nav-link" href="{url}"{current}>{label}</a>'


def menu(label, url, items, active=False):
    if url:
        label_html = nav_link(label, url, active)
        control = f'<summary aria-label="Submenu {label}"></summary>'
    else:
        label_html = ''
        control = f'<summary class="nav-link">{label}</summary>'
    return f'<div class="nav-group">{label_html}<details class="submenu">{control}<ul>{links(items)}</ul></details></div>'


def layout(title, description, path, body):
    is_home = path == '/'
    page_title = 'Scouting Woerden' if is_home else f'{title} | Scouting Woerden'
    logo = f'<img src="{LOGO}" alt="" width="41" height="45"><span>Scouting Woerden<small>Albert Schweitzergroep</small></span>'
    return f'''<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="theme-color" content="#123629">
  <title>{escape(page_title)}</title>
  <link rel="stylesheet" href="/assets/site.css">
  <script src="/assets/site.js" defer></script>
</head>
<body>
<a class="skip-link" href="#inhoud">Direct naar inhoud</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/">{logo}</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="hoofdnavigatie">Menu</button>
    <nav id="hoofdnavigatie" aria-label="Hoofdnavigatie">
      {nav_link('Nieuws', '/#nieuws', is_home)}
      {menu('Lidmaatschap', '/lidmaatschap/', MEMBERSHIP, path.startswith('/lidmaatschap/'))}
      {nav_link('Verhuur', '/verhuur/', path == '/verhuur/')}
      {menu('Algemeen', None, GENERAL)}
      {nav_link('Contact', '/contact/', path == '/contact/')}
    </nav>
  </div>
</header>
<main id="inhoud">{body}</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div><a class="brand" href="/">{logo}</a><address>Kromwijkerdijk 116<br>3448 HW Woerden</address></div>
    <div><h2>Scouting Woerden</h2><ul>{links([('Lidmaatschap', '/lidmaatschap/'), ('Verhuur', '/verhuur/'), ('Contact', '/contact/'), ('Privacyverklaring', GENERAL[4][1])])}</ul></div>
    <div><h2>Volg ons</h2><ul>{links([('Instagram', 'https://www.instagram.com/scoutingwoerden/'), ('Facebook', 'https://www.facebook.com/ScoutingWoerden/'), ('YouTube', 'https://www.youtube.com/@TVScowo'), ('Foto’s', 'https://foto.scowo.nl/')])}</ul></div>
  </div>
</footer>
</body>
</html>
'''


def intro(title, text, eyebrow=''):
    return f'''<section class="page-intro"><div class="wrap">
      <p class="eyebrow">{eyebrow or 'Scouting Woerden'}</p><h1>{title}</h1><p class="lead">{text}</p>
    </div></section>'''


def page(title, text, content, eyebrow=''):
    return intro(title, text, eyebrow) + f'<div class="wrap page-body">{content}</div>'


def news_cards(items):
    return ''.join(
        f'<article class="news-card"><time datetime="{iso}">{date}</time>'
        f'<h3>{link(title, ORIGINAL + path)}</h3><p>{description}</p></article>'
        for date, iso, title, description, path in items
    )


def home():
    date, iso, title, description, path = NEWS[0]
    return f'''
<section class="hero">
  <div class="wrap hero-content">
    <p class="eyebrow">Albert Schweitzergroep · Sinds 1966</p>
    <h1>Samen op avontuur.</h1>
    <p class="lead">Spelen, ontdekken en vrienden maken. Bij Scouting Woerden beleef je buiten meer, op het land én op het water.</p>
    <div class="actions">
      {link('Ontdek de speltakken', '/lidmaatschap/speltakken/', 'button primary')}
      {link('Lid worden', '/lidmaatschap/', 'button outline')}
    </div>
  </div>
</section>
<section class="wrap shortcuts" aria-label="Snel naar">
  <a href="/lidmaatschap/aanmelden-voor-plaatsing/"><strong>Aanmelden</strong><span>Schrijf je in voor de plaatsingslijst</span></a>
  <a href="/verhuur/"><strong>De Boerderij huren</strong><span>Bekijk ons clubhuis en terrein</span></a>
  <a href="/contact/"><strong>Contact opnemen</strong><span>Vind het juiste aanspreekpunt</span></a>
</section>
<section class="wrap news" id="nieuws">
  <div class="section-head"><h2>Nieuws uit onze groep</h2>{link('Naar het nieuwsarchief', ORIGINAL + '/?query-67-page=2', 'text-link')}</div>
  <article class="feature">
    <div class="feature-art"><img src="{POSTER}" alt="Poster van de Goededoelenboomactie" width="724" height="1024" loading="lazy"></div>
    <div class="feature-body"><time datetime="{iso}">{date}</time><h3>{link(title, ORIGINAL + path)}</h3><p>{description}</p>
      {link('Bekijk de Goededoelenboom', 'https://goededoelenboom.nl/', 'button dark')}
    </div>
  </article>
  <div class="news-grid">{news_cards(NEWS[1:])}</div>
</section>
<section class="support"><div class="wrap support-inner"><div><h2>Steun Scouting Woerden</h2><p>Winkel je via SponsorKliks? Dan krijgt onze groep een bijdrage vanuit de webshop.</p></div>
  {link('Naar SponsorKliks', 'https://www.sponsorkliks.com/products/shops.php?club=13497&ref=website', 'button dark')}
</div></section>
'''


def membership():
    data = [
        ('Bevers, Welpen, Esta’s en Dolfijnen', '€ 35,01'),
        ('Paradijsvogels, Verkenners en Explorers', '€ 48,00'),
        ('Ruige vaart, Stam en Plusscouts', '€ 15,00'),
    ]
    rows = ''.join(f'<tr><th scope="row">{label}</th><td>{price}</td></tr>' for label, price in data)
    return page('Lidmaatschap', 'Van een plek op de wachtlijst tot je eerste opkomst. Hier lees je hoe het werkt.', f'''
<div class="text-column">
  <h2>Op de plaatsingslijst</h2><p>Inschrijven kan vanaf de geboorte. In maart en september bieden we kinderen op de lijst een plek aan als er ruimte is. Bij de Bevers kan de wachttijd oplopen tot twee jaar.</p>
  <div class="actions">{link('Aanmelden voor plaatsing', MEMBERSHIP[2][1], 'button dark')}{link('Bekijk de speltakken', MEMBERSHIP[1][1], 'button light')}</div>
  <h2>Eerst meekijken</h2><p>In januari en in mei of juni kun je bij verschillende onderdelen meekijken. Kinderen op de plaatsingslijst krijgen een uitnodiging. Na plaatsing kun je de eerste twee weken gratis meedraaien.</p>
  <h2 id="kosten">Kosten per kwartaal</h2>
  <table><thead><tr><th scope="col">Speltak</th><th scope="col">Contributie</th></tr></thead><tbody>{rows}</tbody></table>
  <p>Kampen, uniform en sommige activiteiten betaal je apart. Op de {link('uitgebreide ledenpagina', ORIGINAL + '/lidmaatschap/#kosten')} staan de bedragen voor kampen en extra’s.</p>
  <p>Voor gezinnen met een lager inkomen zijn er mogelijkheden via de {link('Groene Hart Pas', 'https://www.groenehartpas.nl/uitleg-woerden')} en het {link('Jeugdfonds Sport & Cultuur', 'https://jeugdfondssportencultuur.nl/fondsen/utrecht/')}.</p>
  <h2>Stoppen of overstappen</h2><p>Neem voor een andere groep contact op met {link('plaatsingen@scowo.nl', 'mailto:plaatsingen@scowo.nl')}. Opzeggen kan via {link('de afmeldpagina', MEMBERSHIP[3][1])}.</p>
</div>''')


GROUPS = [
    ('bevers', 'Bevers', '5–7 jaar', 'Buitenspelen, knutselen en voor het eerst een nachtje op kamp.',
     [('Ochtend Bevers', 'Zaterdag · 09.30–11.00'), ('Middag Bevers', 'Zaterdag · 13.15–14.45')]),
    ('dwek', 'Welpen, Esta’s en Dolfijnen', '7–11 jaar', 'Spelen in de jungle, koken op het vuur en pionieren. Dolfijnen gaan ook kanoën en hebben zwemdiploma A nodig.',
     [('Dolfijnen', 'Vrijdag · 18.30–20.30'), ('Ochtend Esta’s', 'Zaterdag · 10.00–12.00'), ('Ochtend Welpen', 'Zaterdag · 10.30–12.30'), ('Middag Esta’s', 'Zaterdag · 14.00–16.00')]),
    ('paradijsvogels', 'Paradijsvogels', '7–13 jaar', 'Een kleine groep met extra begeleiding. We spelen buiten, koken en gaan op ontdekking in de natuur.',
     [('Paradijsvogels', 'Woensdag · 18.30–20.00')]),
    ('verkenners', 'Verkenners', '11–15 jaar · Zeeverkenners tot 18', 'Kampvuur, hikes, zeilen en bouwen met hout en touw. Je leert steeds meer zelf te doen.',
     [('Dinsdagverkenners', 'Dinsdag · 19.00–21.00'), ('Donderdagverkenners', 'Donderdag · 19.00–21.00'), ('Luchtverkenners', 'Zaterdag · 10.00–12.00'), ('Zaterdagmiddagverkenners', 'Zaterdag · 15.00–17.00'), ('Zeeverkenners', 'Zaterdag · zomer 09.00–17.00, winter 11.00–16.00')]),
    ('explorers', 'Explorers', '15–18 jaar', 'De groep organiseert zelf opkomsten en kampen, met een begeleider om mee te denken.',
     [('Vrijdag Explorers', 'Vrijdag · 20.00–22.00')]),
    ('wildevaart', 'Ruige vaart', '18 jaar en ouder', 'Varen, de lelievletten onderhouden en samen activiteiten organiseren.',
     [('Ruige vaart', 'Zaterdag · zomer 10.00–17.00, winter 11.00–16.30')]),
    ('stam', 'Stam', '18–21 jaar', 'Samen activiteiten bedenken en organiseren, zoals de Pooltocht en het Stamcafé.',
     [('Woensdag', '20.00–22.00'), ('Vrijdag', '19.30–21.30')]),
    ('plusscouts', 'Plusscouts', '21 jaar en ouder', 'Blijf betrokken bij de groep en doe mee met activiteiten wanneer het uitkomt.', []),
]


def group_page():
    cards = []
    for slug, title, age, text, times in GROUPS:
        schedule = ''.join(f'<div><dt>{group}</dt><dd>{time}</dd></div>' for group, time in times)
        cards.append(f'<article class="group-card" id="{slug}"><p class="eyebrow">{age}</p><h2>{title}</h2><p>{text}</p>'
                     f'{f"<dl>{schedule}</dl>" if times else ""}</article>')
    return page('Speltakken', 'Elke leeftijd beleeft scouting op zijn eigen manier. Ontdek wat de groepen doen en wanneer ze samenkomen.',
                f'<nav aria-label="Speltakken" class="jump-links">{ "".join(link(title, "#" + slug) for slug, title, *_ in GROUPS)}</nav>'
                f'<div class="group-grid">{"".join(cards)}</div>'
                f'<div class="actions">{link("Aanmelden voor plaatsing", MEMBERSHIP[2][1], "button dark")}{link("Contributie bekijken", "/lidmaatschap/#kosten", "button light")}</div>',
                'Lidmaatschap')


def rental():
    return page('De Boerderij huren', 'Ons clubhuis en het omliggende terrein aan de rand van Woerden zijn te huur voor groepen.', f'''
<div class="info-grid">
<section class="text-column">
  <h2>Gebouw en terrein</h2><p>De Boerderij is de thuisbasis van de Albert Schweitzergroep. Bekijk de rondleiding voor een indruk van het clubhuis en het terrein.</p>
  {link('Bekijk de rondleiding', TOUR, 'button light')}
  <h2>Beschikbaarheid</h2><p>In weekenden houden we tussen 09.00 en 17.00 onze eigen opkomsten op het terrein. Tijdens de zomervakantie gelden andere afspraken. Het verhuurteam bevestigt wat er mogelijk is op jouw datum.</p>
</section>
<aside class="callout"><h2>Reserveren of vragen?</h2><p>Stuur het verhuurteam een mail met je gewenste datum, groepsgrootte en plannen.</p>
  {link('verhuur@scowo.nl', 'mailto:verhuur@scowo.nl', 'button dark')}
</aside></div>''')


def contact():
    addresses = [
        ('Algemeen', 'info@scowo.nl'), ('Plaatsingen', 'plaatsingen@scowo.nl'),
        ('Verhuur', 'verhuur@scowo.nl'), ('Voorzitter', 'voorzitter@scowo.nl'),
        ('Secretaris', 'secretaris@scowo.nl'), ('Penningmeester', 'penningmeester@scowo.nl'),
        ('Locatiebeheer', 'beheerder@scowo.nl'),
    ]
    contacts = ''.join(f'<div><dt>{label}</dt><dd>{link(address, "mailto:" + address)}</dd></div>' for label, address in addresses)
    return page('Contact', 'Een vraag over onze groep, een plaats op scouting of het huren van De Boerderij?', f'''
<div class="info-grid">
<section><h2>Mail ons</h2><dl class="contact-list">{contacts}</dl>
  <p>Voor groepsbegeleiding en vertrouwenspersonen staan de actuele contactgegevens op {link('de contactpagina van Scouting Woerden', ORIGINAL + '/contact/')}.</p>
</section>
<aside class="callout"><h2>Bezoekadres</h2><address>Scouting Woerden<br>Albert Schweitzergroep<br>Kromwijkerdijk 116<br>3448 HW Woerden</address>
  {link('Route naar De Boerderij', ADDRESS, 'button dark')}
</aside></div>''')


def write(path, title, description, body):
    target = ROOT / (path.strip('/') + '/index.html' if path != '/' else 'index.html')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(layout(title, description, path, body), encoding='utf-8')


def main():
    write('/', 'Nieuws', 'Scouting Woerden, de Albert Schweitzergroep. Ontdek onze speltakken, meld je aan en lees het laatste nieuws.', home())
    write('/lidmaatschap/', 'Lidmaatschap', 'Plaatsing, meekijken en contributie bij Scouting Woerden.', membership())
    write(MEMBERSHIP[1][1], 'Speltakken', 'Bekijk de groepen en opkomsttijden van Scouting Woerden.', group_page())
    write(MEMBERSHIP[0][1], 'Over scouting', 'Maak kennis met de Albert Schweitzergroep.', page(
        'Over scouting', 'Buiten spelen en samen iets meemaken, van het eerste kampvuur tot zelf een kamp organiseren.',
        f'<div class="text-column"><h2>Scouting in Woerden</h2><p>De Albert Schweitzergroep is actief sinds 1966. Onze thuisbasis is De Boerderij aan de Kromwijkerdijk. Er zijn groepen die vooral op het land spelen en groepen die veel op het water zijn.</p><p>Vrijwilligers organiseren de opkomsten, kampen en groepsactiviteiten. Alle vrijwilligers hebben een Verklaring Omtrent Gedrag.</p><div class="actions">{link("Bekijk de speltakken", MEMBERSHIP[1][1], "button dark")}</div></div>',
        'Lidmaatschap'))
    write(MEMBERSHIP[2][1], 'Aanmelden voor plaatsing', 'Meld je aan voor de plaatsingslijst van Scouting Woerden.', page(
        'Aanmelden voor plaatsing', 'Schrijf je kosteloos en vrijblijvend in voor de plaatsingslijst.',
        f'<div class="text-column"><p>Inschrijven kan vanaf de geboorte. In maart en september komen er plaatsen vrij. Als er een passende plek is, krijg je bericht en kun je die aannemen of op de lijst blijven.</p><div class="actions">{link("Open het aanmeldformulier", SIGNUP, "button dark")}</div><p>Vragen? Mail {link("plaatsingen@scowo.nl", "mailto:plaatsingen@scowo.nl")}.</p></div>',
        'Lidmaatschap'))
    write(MEMBERSHIP[3][1], 'Lidmaatschap afmelden', 'Zeg je lidmaatschap op via het afmeldformulier van Scouting Woerden.', page(
        'Lidmaatschap afmelden', 'Via het afmeldformulier kun je het lidmaatschap opzeggen.',
        f'<div class="text-column"><p>Het lidmaatschap loopt per kwartaal. Na opzegging stopt de contributie aan het einde van het kwartaal. Wil je liever overstappen naar een andere speltak? Mail dan {link("plaatsingen@scowo.nl", "mailto:plaatsingen@scowo.nl")}.</p><div class="actions">{link("Open het afmeldformulier", CANCEL, "button dark")}</div></div>',
        'Lidmaatschap'))
    write('/verhuur/', 'Verhuur', 'Huur De Boerderij en het terrein van Scouting Woerden.', rental())
    write('/contact/', 'Contact', 'Adres en contactgegevens van Scouting Woerden.', contact())
    (ROOT / '404.html').write_text(layout('Pagina niet gevonden', 'Pagina niet gevonden.', '/404',
        page('Pagina niet gevonden', 'Je kunt terug naar het nieuws of verder zoeken op de oorspronkelijke site.',
             f'<div class="actions">{link("Naar de homepage", "/", "button dark")}{link("Naar scowo.nl", ORIGINAL, "button light")}</div>')),
        encoding='utf-8')


if __name__ == '__main__':
    main()
