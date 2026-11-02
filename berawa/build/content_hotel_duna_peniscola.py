# Contenido de la demo Duna Hotel Boutique (Peñíscola) (es/en/fr/de). Hechos de dunahotel.es leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Doble y doble con balcón','Con vistas al mar','Doble Deluxe'],'en':['Double and double with balcony','Sea view','Deluxe Double'],'fr':['Double et double avec balcon','Vue mer','Double Deluxe'],'de':['Doppelzimmer und Doppelzimmer mit Balkon','Meerblick','Doppelzimmer Deluxe']}
RD={
'es':['17 m², con vista interior o balcón a la calle Río. Aire acondicionado, minibar, caja fuerte y limpieza diaria.','Vistas al castillo y a la playa Norte de Peñíscola, desde la ventana o desde el balcón.','21 m², la única con bañera además de la ducha, con albornoces; también hay versión con vistas al mar.'],
'en':['17 m², with an inner view or a balcony onto calle Río. Air conditioning, minibar, safe and daily cleaning.','Views of the castle and Peñíscola’s North beach, from the window or the balcony.','21 m², the only one with a bathtub as well as a shower, with bathrobes; also available with sea view.'],
'fr':['17 m², vue intérieure ou balcon sur la calle Río. Climatisation, minibar, coffre-fort et ménage quotidien.','Vue sur le château et la plage Nord de Peñíscola, depuis la fenêtre ou le balcon.','21 m², la seule avec baignoire en plus de la douche, avec peignoirs ; existe aussi avec vue mer.'],
'de':['17 m², mit Innenblick oder Balkon zur Calle Río. Klimaanlage, Minibar, Safe und tägliche Reinigung.','Blick auf die Burg und den Nordstrand von Peñíscola, vom Fenster oder Balkon.','21 m², als einziges mit Badewanne zusätzlich zur Dusche, mit Bademänteln; auch mit Meerblick.']}
ART={
'hero':('waves',1711,['#0f2c3d','#3f8fb5','#e3f1f7','#3a6e85','#24546b','#0a1e2a']),
'intro':('skyline',1712,['#f2f6f8','#f9fbfc','#1f5e7d','#4f5f68','#1b2c35']),
'r1':('columns',1721,['#f2f6f8','#f9fbfc','#1f5e7d','#4f5f68','#1b2c35']),
'r2':('waves',1722,['#0f2c3d','#4a9cc2','#e8f4f9','#427a92','#2a5b72','#0a1e2a']),
'r3':('arches',1723,['#f4efe6','#e7d7bd','#1f5e7d','#5d5a52','#2b2a24']),
'g1':('skyline',1731,['#0f2c3d','#3f8fb5','#e3f1f7','#3a6e85','#24546b','#0a1e2a']),
'g2':('waves',1732,['#0f2c3d','#4a9cc2','#e8f4f9','#427a92','#2a5b72','#0a1e2a']),
'g3':('hills',1733,['#eef2ea','#dde6d4','#9db48a','#7c8a6c','#5a654d','#394030']),
'g4':('columns',1734,['#f2f6f8','#f9fbfc','#1f5e7d','#4f5f68','#1b2c35'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Duna Hotel Boutique · Primera línea de playa en Peñíscola',see_rooms='Ver habitaciones',hero_k='Peñíscola · Avda. del Mar, 35',hero_t='Paz y relajación junto al mar en Peñíscola',hero_s='En primerísima línea de playa, a escasos 200 metros del Casco Antiguo.',
 intro_t='Un hotel boutique de trato familiar',intro_p1='20 habitaciones en dos plantas, decoradas en estilo mediterráneo minimalista y reformadas totalmente en junio de 2018.',
 intro_p2='Wifi gratis en todas las habitaciones y en recepción, ascensor a las plantas y un trato familiar para que te sientas como en casa.',
 stats=['20 habitaciones','Primera línea de playa','A 200 m del Casco Antiguo','Reformado en 2018'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Para dos personas, con baño privado con ducha a ras de suelo, aire acondicionado y calefacción, Smart TV, wifi gratis, minibar y caja fuerte.',
 svcs=['Wifi gratis en habitaciones y recepción','Ascensor a las plantas de habitaciones','Cuna sin coste en algunas habitaciones','Guarda de bicicletas','Limpieza diaria','Recepción de 8:00 a 24:00 en verano'],
 loc_p='Avda. del Mar, 35 · 12598 Peñíscola (Castellón). Teléfono: 964 480 205. Correo: reservas@dunahotel.es.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis parking?','¿A qué hora es el check-in?','¿Cómo reservo?']),
'en':dict(title='Duna Hotel Boutique · Beachfront in Peñíscola',see_rooms='See rooms',hero_k='Peñíscola · Avda. del Mar, 35',hero_t='Peace and relaxation by the sea in Peñíscola',hero_s='Right on the beachfront, just 200 metres from the Old Town.',
 intro_t='A family-run boutique hotel',intro_p1='20 rooms on two floors, decorated in minimalist Mediterranean style and fully renovated in June 2018.',
 intro_p2='Free wifi in every room and at reception, a lift to the room floors and a family welcome to make you feel at home.',
 stats=['20 rooms','Beachfront','200 m from the Old Town','Renovated in 2018'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='For two people, with private bathroom with walk-in shower, air conditioning and heating, Smart TV, free wifi, minibar and safe.',
 svcs=['Free wifi in rooms and at reception','Lift to the room floors','Free cot in some rooms','Bicycle storage','Daily cleaning','Reception 8:00 to 24:00 in summer'],
 loc_p='Avda. del Mar, 35 · 12598 Peñíscola (Castellón). Phone: +34 964 480 205. Email: reservas@dunahotel.es.',
 chips=['Which rooms do you have?','Do you have parking?','What time is check-in?','How do I book?']),
'fr':dict(title='Duna Hotel Boutique · Front de mer à Peñíscola',see_rooms='Voir les chambres',hero_k='Peñíscola · Avda. del Mar, 35',hero_t='Calme et détente au bord de la mer à Peñíscola',hero_s='En tout premier rang face à la plage, à 200 mètres de la vieille ville.',
 intro_t='Un hôtel boutique à l’accueil familial',intro_p1='20 chambres sur deux étages, décorées dans un style méditerranéen minimaliste et entièrement rénovées en juin 2018.',
 intro_p2='Wifi gratuit dans toutes les chambres et à la réception, ascenseur vers les étages et un accueil familial pour vous sentir comme chez vous.',
 stats=['20 chambres','Front de mer','À 200 m de la vieille ville','Rénové en 2018'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Pour deux personnes, avec salle de bains privée et douche à l’italienne, climatisation et chauffage, Smart TV, wifi gratuit, minibar et coffre-fort.',
 svcs=['Wifi gratuit en chambre et à la réception','Ascenseur vers les étages','Lit bébé gratuit dans certaines chambres','Garde des vélos','Ménage quotidien','Réception de 8:00 à 24:00 en été'],
 loc_p='Avda. del Mar, 35 · 12598 Peñíscola (Castellón). Téléphone : +34 964 480 205. E-mail : reservas@dunahotel.es.',
 chips=['Quelles chambres avez-vous ?','Avez-vous un parking ?','À quelle heure est le check-in ?','Comment réserver ?']),
'de':dict(title='Duna Hotel Boutique · Direkt am Strand in Peñíscola',see_rooms='Zimmer ansehen',hero_k='Peñíscola · Avda. del Mar, 35',hero_t='Ruhe und Entspannung am Meer in Peñíscola',hero_s='In erster Strandlinie, nur 200 Meter von der Altstadt.',
 intro_t='Ein familiär geführtes Boutique-Hotel',intro_p1='20 Zimmer auf zwei Etagen, im minimalistischen Mittelmeerstil eingerichtet und im Juni 2018 komplett renoviert.',
 intro_p2='Kostenloses WLAN in allen Zimmern und an der Rezeption, Aufzug zu den Etagen und familiäre Gastfreundschaft, damit Sie sich wie zu Hause fühlen.',
 stats=['20 Zimmer','Erste Strandlinie','200 m zur Altstadt','2018 renoviert'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Für zwei Personen, mit eigenem Bad mit bodengleicher Dusche, Klimaanlage und Heizung, Smart-TV, kostenlosem WLAN, Minibar und Safe.',
 svcs=['Kostenloses WLAN in Zimmern und Rezeption','Aufzug zu den Zimmeretagen','Kostenloses Kinderbett in einigen Zimmern','Fahrradaufbewahrung','Tägliche Reinigung','Rezeption im Sommer 8:00 bis 24:00'],
 loc_p='Avda. del Mar, 35 · 12598 Peñíscola (Castellón). Telefon: +34 964 480 205. E-Mail: reservas@dunahotel.es.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Parkplatz?','Wann ist der Check-in?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://reservas.dunahotel.es/'
BOOK=dict(mode='engine',url=dict(es=RB+'es/',en=RB+'en/',fr=RB+'fr/',de=RB+'de/'))
D=dict(name='Duna Hotel Boutique',ac='#0f2c3d',ac2='#1f5e7d',ac2_a11y='#1a5370',book=BOOK,around=[],foot=FOOT,
 address='Avda. del Mar, 35 · 12598 Peñíscola',phones=['+34 964 480 205'],emails=['reservas@dunahotel.es'],maps='Duna Hotel Boutique, Avenida del Mar 35, 12598 Peñíscola',t=T)
META=dict(repo='demo-hotel-duna-peniscola',name='Duna Hotel Boutique',legal_name='Hostelera de Peñíscola SL, CIF B44505022 (aviso legal de su web)',registry_ids=['B44505022'],
 url='https://dunahotel.es/',domain='dunahotel.es',municipality='Peñíscola',province='Castellón',sector='hotel boutique en primera línea de playa en Peñíscola',
 read_at='2026-11-02T11:00:00+01:00',created_at='2026-11-02T10:59:00+01:00',built_at='2026-11-02T11:20:00+01:00',audit_date='2026-11-02T11:00:00+01:00',
 rating=dict(value=4.3,coincide=['tel','web'],date='2026-10-30',url='https://www.google.com/maps/search/Duna+Hotel+Pe%C3%B1%C3%ADscola'),
 book=dict(mode='engine',url=RB+'es/',note='motor propio enlazado desde el boton RESERVAR de su web: https://reservas.dunahotel.es/es/ (es), /en/, /fr/ y /de/, HTTP 200 los cuatro (02/11/2026 11:05).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Tenéis parking?','K03'),('¿Tenéis piscina?','K04'),('¿Hay desayuno?','K05'),('¿A qué hora es el check-in?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Puedo cancelar la reserva?','K09'),('¿Admitís mascotas?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Tenéis cuna?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis gimnasio?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Do you have parking?','K03'),('Do you have a pool?','K04'),('Is there breakfast?','K05'),('What time is check-in?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Can I cancel my booking?','K09'),('Do you allow pets?','K10'),('What is your phone number?','K11'),('Do you have a cot?','K12'),('How much is a night?',None),('Do you have a gym?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Avez-vous un parking ?','K03'),('Avez-vous une piscine ?','K04'),('Y a-t-il un petit-déjeuner ?','K05'),('À quelle heure est le check-in ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Puis-je annuler ma réservation ?','K09'),('Acceptez-vous les animaux ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Avez-vous un lit bébé ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une salle de sport ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Gibt es einen Parkplatz?','K03'),('Haben Sie einen Pool?','K04'),('Gibt es Frühstück?','K05'),('Wann ist der Check-in?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Kann ich meine Buchung stornieren?','K09'),('Sind Haustiere erlaubt?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Haben Sie ein Kinderbett?','K12'),('Was kostet eine Nacht?',None),('Gibt es einen Fitnessraum?',None)]}
