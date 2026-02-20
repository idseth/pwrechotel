# %%writefile GeneraDatasetLiv1.py
# %%writefile GeneraDatasetLiv1.py - comando speciale di jupyter per creare file .py da aggiungere come prima riga dello script

import csv         # Modulo standard di Python per leggere e scrivere file CSV
import itertools   # Strumenti per lavorare con iteratori e combinazioni. Serve soprattutto a generare combinazioni di varianti

# Funzione per generare tutte le combinazioni possibili da una frase con varianti
# Le varianti sono indicate con parole separate da slash, es: "pulita/ordinata"
def genera_varianti(frase):
    parti = []                             # parti conterrà una lista di liste
    for token in frase.split():            # Separa la frase in token
        if '/' in token:                   # e cerca all'interno dei token il carattere /
            varianti = token.split('/')    # Separa le varianti
            parti.append(varianti)
        else:
            parti.append([token])
    combinazioni = list(itertools.product(*parti))               # l'* spacchetta la lista di liste e intertools.product ne fa il prodotto cartesiano
    frasi_generate = [' '.join(comb) for comb in combinazioni]   # list comprehension: riassembla le tuple contenute in "combinazioni"
    return frasi_generate

# Frasi base con varianti per reparto e sentiment
frasi_base = {                   # dizionario
    'Housekeeping': {            # che contiene 3 chiavi e 3 dizionari
        'pos': [                 # che contengono 2 chiavi e 2 liste che contengono le recensioni
            "Camera/Stanza pulita e ordinata; personale cordiale/gentile e disponibile.",                                     # 4  
            "Albergo/Hotel confortevole e accogliente. Pulizia impeccabile e attenzione/accortezza ai dettagli.",             # 4
            "Tutto il personale è stato cordiale/gentile e premuroso! Ottima pulizia della stanza.",                          # 2
            "Atmosfera confortevole e personale disponibile. Bagno/Servizi e camera puliti ogni giorno. Consigliatissimo!",   # 2
            "Stanza/Sistemazione in ordine e ben curata; ottima struttura ed ottimi servizi.",                                # 2
            "Cura della stanza perfetta. Attenzione ai dettagli e professionalità/serietà.",                                  # 2
            "Camera confortevole/comoda e dipendenti sempre disponibili/gentili.",                                            # 4 -> 20
            "Massimo/Grande confort non solo in camera ma in tutta la struttura. Atmosfera calda/accogliente e rilassante.",  # 4
            "Servizio di cambio biancheria/asciugamani giornaliero/quotidiano. Bagno e camera sempre in ordine.",             # 4
            "Ambiente/Contesto pulito e tranquillo, ideale per chi ha bisogno di rilassarsi/riposarsi.",                      # 4
            "Sono allergica alla polvere e con mia grande sorpresa/felicità non ne ho trovata la minima traccia!",            # 2                 
            "Bagno in camera con doccia e vasca sempre puliti; arredi/mobili nuovi, belli e funzionali.",                     # 2
            "Servizio di manutenzione impeccabile. Camera sempre in ordine e tutto funzionante alla perfezione.",             # 1
            "Bagno/Servizi e camera sempre puliti. Struttura accogliente e piacevole.",                                       # 2
            "Igiene irreprensibile/ineccepibile e massima disponibilità da parte dei dipendenti dell'albergo/hotel.",         # 4
            "Cura in ogni dettaglio dell'arredamento. Ambienti spaziosi e sempre in ordine.",                                 # 1
            "Arredi delle camere moderni e funzionali. Struttura nuova e ben tenuta.",                                        # 1
            "Camera molto bella e spaziosa, pulita ed in ordine. Ottimo personale.",                                          # 1
            "Ambienti puliti e decorosi. Personale serio/affidabile e preparato.",                                            # 2
            "Camera già pronta al mio arrivo ed in perfette/ottime condizioni. Ottimo rapporto qualità-prezzo.",              # 2 -> 50
            "Hotel confortevole, pulito e a buon prezzo. Posizione strategica a due passi dal centro.",                       # 1
            "Siamo stati sistemati in due comodissime camere comunicanti ideali per una famiglia.",                           # 1
            "Hotel dotato di ogni comfort, pulizia estrema, camere ampie, nuove e ben arredate.",                             # 1
            "Una perla rara in termini/fatto di attenzione al cliente, comodità/confort e pulizia delle camere.",             # 4
            "Hotel ricco di semplici/piccoli dettagli che rendono estremamente confortevole il soggiorno.",                   # 2
            "Struttura comoda e con personale cortese/gentile. Camere spaziose. Perfetto per un viaggio di lavoro.",          # 2
            "Ambiente tranquillo/silenzioso, personale disponibile, stanze ben curate e sempre in ordine.",                   # 2
            "Atmosfera classica e arredi delle camere in legno rendono l'ambiente molto accogliente.",                        # 1
            "Camera piacevole ed accogliente, con una curiosa (ma funzionale) grande doccia/vasca esterna al bagno.",         # 2
            "Pulizia/Igiene e ottimo rapporto qualità-prezzo.",                                                               # 2                   
            "Stanze con tutti i requisiti/pregi, confortevoli e ben curate/tenute. Bella esperienza.",                        # 4
            "Camera, bagno e doccia molto spaziosi e ben arredati.",                                                          # 1
            "Stanze pulite e accoglienti, arredate in legno stile classico, danno una bella sensazione di calore.",           # 1
            "Camera confortevole e silenziosa/tranquilla, albergo/struttura in ottima posizione. Promosso in pieno.",         # 4
            "Ottimo hotel, arredato finemente e con grande focus sull'igiene.",                                               # 1
            "Struttura ricettiva in cui nulla è lasciato al caso. Ottima la pulizia, estrema gentilezza, tranquillità.",      # 1 -> 80
            "Albergo molto/parecchio/realmente confortevole. Camera ben riscaldata e silenziosa.",                            # 3
            "Ambiente pulito e ordinato. Voto 10! Consigliato/Promosso!",                                                     # 2
            "La camera era spaziosa, ben arredata e pulita, così conme pure i servizi igienici.",                             # 1
            "Letto comodo/confortevole e stanza grande. Ottimo pernottamento/soggiorno.",                                     # 4
            "Non manca nessun confort: camere arredate elegantemente, bagni nuovi e doccia molto spaziosa.",                  # 1
            "hotel carino e ben curato/tenuto. Camere silenziose e ben arredate/ammobiliate.",                                # 4
            "Accoglienza, comfort e praticità. Stanza comoda e funzionale.",                                                  # 1
            "L'hotel è molto bello: pulito, nuovo, ben arredato e comodo.",                                                   # 1
            "Molto accogliente e dai contorni sobri. Eccellente la camera riservataci.",                                      # 1
            "Materasso ortopedico ideale per riposare bene. Bagno piccolo ma pulito.",                                        # 1
            "Nessuna traccia di polvere o sporcizia in nessun angolo della camera. Controllato personalmente.",               # 1
            "Le camere sono dotate di TV a schermo piatto, aria condizionata e minibar per il massimo comfort.",              # 1
            "L'arredamento è accogliente, con interni di alta qualità e camere sempre immacolate. Relax totale.",             # 1
            "Ambiente caldo e familiare molto ben curato/tenuto, ideale/perfetto per famiglie.",                              # 4
            "Pulizia impeccabile/ineccepibile, uno dei migliori pernottamenti mai fatti.",                                    # 2
            "Camera meravigliosa/stupenda, arredata con cura e attenzione e con tutto il necessario al suo interno.",         # 2 -> 110
            "Camera pulita e confortevole con ottima vista panoramica. Personale di pulizia sempre presente e disponibile.",  # 1
            "Camera Executive con vista, curata, pulita/immacolata e ben arredata.",                                          # 2
            "Servizio lavanderia, tv e aria condizionata, frigobar ben fornito e wifi. Ottimo soggiorno.",                    # 1
            "Camera molto pulita e confortevole/accogliente attrezzata con tutto ciò di cui potresti avere bisogno.",         # 2
            "Albergo accogliente, pulito e attrezzato. Personale disponibile/gentile e attento a qualsiasi esigenza.",        # 2
            "B&b super accogliente, camere pulite e arredate/sistemate con cura.",                                            # 2
            "Ottima struttura ricettiva. La camera era immacolata con una doccia eccellente.",                                # 1
            "Struttura stupenda che ti fa sentire come a casa. Ambiente familiare pulito e tranquillo.",                      # 1
            "L'albergo è ottimo e ben tenuto. Camere piccole ma molto accoglienti/confortevoli.",                             # 2
            "Ottimo B&B/hotel/residence con ottimo personale. Stanza pulita e ben sistemata/attrezzata.",                     # 6
            "Albergo molto bello, inoltre la stanza è super pulita e molto accogliente con il suo arredamento moderno.",      # 1
            "Soggiorno fantastico in questo B&B. La camera/stanza era molto pulita, nulla da ridire/obiettare!",              # 4
            "Camera PERFETTA, pulitissima e dotata di ogni comfort/comodità, ma proprio tutti!",                              # 2
            "Bagno in camera super attrezzato. Struttura 10, pulizia 10.",                                                    # 1
            "Struttura ed arredamento nuovi, camera/stanza pulita ed ordinata, accoglienza familiare.",                       # 2 
            "Albergo fantastico/stupendo, pulizia eccellente. Promosso in pieno/toto!",                                       # 4                              
            "Personale di pulizia sempre disponibile/pronto per ogni esigenza/necessità.",                                    # 4
            "Residence nuovo e ben gestito. Pulizia e cordialità. Pomosso a pieni voti.",                                     # 1
            "La camera è davvero spaziosa e ha buone finestre spesse per garantire una notte di sonno tranquilla.",           # 1
            "Sistemazione perfetta, camera pulita e con letto molto comodo! Voto 10.",                                        # 1
            "Struttura super pulita e molto ben attrezzata. voto 9 su 10!",                                                   # 1 -> 150
            "Fantastico/ottimo/stupendo B&B, pulitissimo, super organizzato e camere molto belle.",                           # 3  
            "Una struttura nuova e in centro città. Camera perfetta/ottima e pulitissima.",                                   # 2
            "Struttura 9, pulizia 10. Promosso!",                                                                             # 1
            "L'albergo è accogliente e la camera luminosa, molto/ben pulita e con un bel balconcino alla francese.",          # 2
            "Doccia e camera molto comode ed è evidente la recente ristrutturazione/risistemazione dell'albergo.",            # 2
            "Accoglienza ttima/meravigliosa, camere molto belle e pulizia impeccabile! Ritorneremo sicuramente.",             # 2
            "Camera arredata modernamente e molto pulita. Massimo/ottimo confort anche in bagno.",                            # 2 
            "Camere accoglienti, pulite, dotate di macchinetta del caffè e, nonostante l'affaccio su strada, molto silenziose.",#1
            "Ottima ospitalità. Adoro la camera, adoro la posizione. Sceglierò di nuovo questo B&B.",                         # 1
            "Molto pulito, tranquillo/silenzioso, ottimo wifi e un letto comodo. Bagno un po' piccolo ma funzionale.",        # 2
            "Camera/Sistemazione perfetta, pulizia ottima/massima.",                                                          # 4
            "Grazie a tutti i confort sono rimasto più a lungo di quanto previsto! Voto 9, pulizia 9.",                       # 1
            "La camera era perfetta, pulita quotidianamente dal personale. Bellissima esperienza.",                           # 1
            "Camera nuova, pulita e confortevole. Posizione/luogo/località eccellente. Giudizio positivo.",                   # 3
            "Mi è piaciuta molto la camera, con letti molto comodi, pulitissima e con servizio per fare caffè.",              # 1
            "Segnalo l'ottima pulizia, serietà, efficienza, competenza e disponibilità.",                                     # 1
            "Struttura assolutamente perfetta in fatto di pulizia/igiene e confort/comodità.",                                # 4
            "La sistemazione/struttura è come indicato. Ottimamente arredato, molto pulito e curato.",                        # 2
            "Soggiorno semplicemente perfetto. La struttura è stupenda/bellissima, pulitissima, nuova e molto comoda.",       # 2
            "Struttura curata/seguita in ogni minimo dettaglio. Non avrei potuto chiedere/sperare di meglio.",                # 4
            "Albergo curato nei minimi particolari/dettagli. Camera è arredata con gusto, comoda e spaziosa!",                # 2
            "Camere colorate ed eleganti, bagni nuovi, confort e disponibilità assolute/totale.",                             # 2
            "Stanza e hotel pulitissimi e molto accoglienti.",                                                                # 1
            "Camere in legno, pulite e accoglienti, con finestre affacciate sulla piazza/zona centrale.",                     # 2
            "Camera pulita e silenziosa/tranquilla con bellissimo balconcino privato.",                                       # 2 -> 200
            "Struttura accogliente a due/pochi passi dal centro. Camere confortevoli e fuonzionali.",                         # 2
            "L'hotel era molto bello, le camere sono molto pulite e silenziose.",                                             # 1
            "Camera e bagno nuovi e confortevoli. Ottima pulizia in tutti gli ambienti/spazi.",                               # 2
            "Camere tutte molto carine/belle ed ognuna con affaccio sul paese. Bella esperienza.",                            # 2
            "Ottimo/perfetto trattamento, bella la camera, arredata in stile tirolese, massima puliza.",                      # 2
            "Soggiornato 2 notti e 3 giorni, pro: pulito e ben organizzato.",                                                 # 1
            "L’appartamento/alloggio spazioso e impeccabilmente pulito, con una terrazza con vista mozzafiato.",              # 1
            "Bellissimo appartamento, camere tutte spaziose, pulite e con una vista stupenda.",                               # 1
            "L’ambiente è molto accogliente e confortevole, luminoso e la posizione/collocazione è ottima.",                  # 2
            "Questo hotel è una vera gemma/perla! Camere confortevoli e un eccellente servizio.",                             # 2
            "Sistemazione perfetta! Pulita, accogliente e in posizione fantastica.",                                          # 1
            "Mi sono sentito come a casa. Appartamento pulito e ben arredato.",                                               # 1
            "Appartamento esattamente come in foto: moderno, luminoso, spazioso, pulito e molto ben arredato.",               # 1
            "Letto/materasso comodissimo, confort e pulizia. Ospitalità perfetta.",                                           # 2
            "Ottima esperienza, camera con spazio sufficiente per quattro persone e condizioni impeccabili.",                 # 1
            "L’ambiente è accogliente e silenzioso, ideale/perfetto per rilassarsi. Consiglio vivamente.",                    # 2
            "La camera in cui ho alloggiato era spaziosa, ben arredata e soprattutto pulita.",                                # 1
            "La camera è semplicemente perfetta. Un ambiente caldo e accogliente, arredato con materiali di pregio.",         # 1
            "Letto incredibilmente comodo, garantisce un sonno riposante dopo lunghe giornate di esplorazione.",              # 1
            "Tanta cortesia/gentilezza/professionalità e ottima pulizia delle camere.",                                       # 3 -> 230
            "Bello l'ambiente, belle le camere, tutto perfetto/impeccabile/eccellente.",                                      # 3
            "Hotel delizioso/incantevole, bellissima atmosfera; camere grandi e lussuose con vista.",                         # 2
            "Abbiamo soggiornato in questo hotel cinque notti. I letti sono comodi, la pulizia impeccabile.",                 # 1
            "Hotel bellissimo... Pulizia estrema e cura dei dettagli/particolari da ammirare/lodare.",                        # 4
            "TUTTO PERFETTO/ECCEZIONALE, camera e bagno/servizi stupendi/magnifici.",                                         # 8
            "Hotel molto comodo. Camera abbastanza ampia, con bel terrazzino arredato e stendibiancheria.",                   # 1
            "Hotel consigliatissimo/raccomandato. Stanza molto apprezzata/gradita e confortevole.",                           # 4                
            "Albergo accogliente con ottimo rapporto qualità prezzo. Camere pulitissime e personale cortese.",                # 1
            "letti matrimoniali comodi e un ampio/grande bagno. Pulizia direi più che ottima/perfetta.",                      # 2
            "L’hotel è molto curato e pulito. Vacanza all’insegna del comfort e di piccole attenzioni quotidiane.",           # 1
            "L'hotel è nuovo e ristrutturato di recente; camere molto belle, pulite e con tutto ciò che serve.",              # 1
            "Struttura molto accogliente e pulita, camera molto curata nei dettagli, ottima idea lo spazio cabina armadio.",  # 1
            "Bagno nuovo con doccia molto spaziosa. Ottima pulizia. Complimenti a tutto lo staff!",                           # 1
            "Dalla prima accoglienza, si percepisce un’atmosfera intima e curata.",                                           # 1
            "Personale/servizio di pulizia impeccabile. Pulizia eccellente",                                                  # 2
            "Pulizia massima/elevata e camere sempre in ordine",                                                              # 2 = 133 -> 265
        ],
        'neg': [
            "Camera/stanza sporca/sudicia e disordinata/trasandata.",                                                         # 8
            "Struttura/Sistemazione trasandata e poco/non pulita.",                                                           # 4
            "Personale poco attento/accorto alla pulizia delle camere e dei bagni.",                                          # 2
            "Mancanza/Assenza di igiene nelle camere; lenzuola macchiate/imbrattate e bagno sporco.",                         # 4
            "Questo è il posto con le condizioni igieniche generali del bagno peggiori che io abbia mai visto.",              # 1
            "Porte rotte/danneggiate e tendina della doccia diventata grigia/marrone per lo sporco e la muffa.",              # 4
            "Coperchio del water rotto/guasto per ossidazione e marroncino per lo sporco. Disgustoso/Terribile.",             # 4
            "Fughe/linee delle piastrelle/mattonelle della doccia nere per lo sporco e la mancata pulizia.",                  # 4
            "Pareti scrostate e da cui cadevano pezzi/parti di intonaco.",                                                    # 2
            "Spazzolone/Scopino per pulire il bagno, vecchio, quasi completamente consumato e… nero!",                        # 2
            "Moquette in stanza in gran/buona parte rotta, sporca e rabberciata in qualche maniera.",                         # 2
            "Tappeti logori/usurati e pieni/colmi di polvere.",                                                               # 4
            "Moquette, sia quella sul pavimento che quella alle pareti, logora/rovinata e sporca.",                           # 2
            "Le stanze e i corridoi non vedono una imbiancatura/tinteggiatura da anni/secoli.",                               # 4
            "Stabile/edificio logoro, in pessime condizioni e lasciato andare alla deriva.",                                  # 2
            "Doccia con la tendina scomoda perché si rischia di allagare il bagno. Albergo senza troppe pretese.",            # 1 -> 50
            "Condizioni igieniche del bagno penose/pessime. Mai visto nulla di simile.",                                      # 2
            "Una stanza così non può e non deve essere considerata abitabile. Pessime condizioni, pessima igiene.",           # 2
            "Camere e bagno super/molto sporchi. Assolutamente vergognoso! Evitatelo.",                                       # 2
            "Moquette sporchissima e bagno lurido. Esperienza da non ripetere!",                                              # 1
            "La struttura non è né molto nuova/recente, né molto pulita. Voto 5 per me.",                                     # 2
            "Rapporto qualità prezzo altamente negativo. Struttura (e camere in particolare) un po' abbandonata.",            # 1
            "le camere sono molto piccole e spartane, anche vecchiotte, non un granché insomma.",                             # 1
            "L'albergo ha bisogno di aggiornamenti e riparazioni. Hall vecchia e camere molto datate.",                       # 1
            "La doccia aveva segni terribili vecchio stampo di arancia e l'acqua scorre fuori sporcando tutto il bagno.",     # 1
            "Condizionatore d'aria molto rumoroso/fastidioso che a causa di una perdita ha allagato la moquette.",            # 2
            "Ho soggiornato qui anni prima ed era molto più pulito rispetto ad ora.",                                         # 1
            "Stanza piuttosto buia (non luminosa) e poco accogliente/ospitale.",                                              # 2
            "Pochi comfort, niente lussi e 0 pulizie extra. Probabilmente non tornerò.",                                      # 1
            "Questo albergo non è terribile ma sicuramente ci sono molte cose da rivedere, a cominciare dalle pulizie!",      # 1
            "Stanze rumorose/chiassose e poco curate. Poca attenzione ai dettagli.",                                          # 2
            "Camera poco pulita e bagno fuori servizio. Terribile/Tremendo/Penoso.",                                          # 3
            "Arredi vetusti/sgangherati e poco funzionali. Camere vecchie da ristrutturare/risistemare.",                     # 4
            "Hotel vecchissimo - moquette mangiucchiata e staccata qui e lì (attenzione a non inciampare). Da evitare!",      # 1
            "Camera sporca in ogni angolo/dove; niente ascensore e zanzare/insetti nella stanza.",                            # 4
            "Muri della stanza macchiati di insetti morti (ancora attaccati).",                                               # 1
            "Bagno in camera senza bidet! Sveglia, siamo in Italia!",                                                         # 1
            "L'hotel è molto vecchio e ha sicuramente bisogno di un ascensore; la camera e il bagno necessitano un rinnovo.", # 1
            "Non lo consiglierei. Pulizie scarse/approssimative e arredamenti vecchi e fatiscenti.",                          # 2
            "Camere sporche, moquette rialzata da terra, muri sporchi/macchiati. Non lo consiglierei.",                       # 2
            "Il peggior hotel/albergo in cui ho soggiornato. Biancheria da letto sudicia e macchiata.",                       # 2
            "Puzza/odore terribile in camera. Atmosfera vecchia e opprimente. Siamo fuggiti.",                                # 2
            "E' stato un susseguirsi/succedersi di pessime impressioni! Hotel molto antiquato/obsoleto.",                     # 4
            "Moquette scolorita e rivestimenti datati, la camera era davvero angusta, per non parlare del bagno.",            # 1 -> 100
            "Camera con finestre che non si chiudevano bene e invasa dalle zanzare. Esperienza da non ripetere.",             # 1
            "Struttura fatiscente, moquette sporca e consumata, materasso sfondato, cuscini quasi inesistenti.",              # 1
            "Albergo fatiscente al limite dell' agibile! Stanze vecchie mai restautare, pulizia opinabile/discutibile.",      # 2
            "La nostra camera aveva un handicap doccia. L'asta era caduta e c'era muffa ovunque/dappertutto.",                # 2
            "Il telaio della finestra è ammuffito e rovinato/rotto. I letti non sono confortevoli/comodi.",                   # 4
            "I cuscini sono in disperato bisogno di sostituzione/ricambio. Zanzariere alle finestre rotte e non efficaci.",   # 2
            "Bagno piccolo e non confortevole, senza piatto doccia e con tendina sporca.",                                    # 1
            "La camera, come tutto l'albergo, è abbastanza spoglia. Le pulizie lasciano a desiderare.",                       # 1
            "I servizi sono un po carenti/scarsi. Camera spartana e poco accogliente.",                                       # 2
            "Camera piccola e non confortevole. Arredi vecchi e mal tenuti/conservati.",                                      # 2
            "Bagno non troppo pulito e con illuminazione/luce scarsa. Ambiente scadente/mediocre.",                           # 4
            "Struttura fatiscente, moquette ovunque che non dà il benché minimo senso di pulizia/igiene.",                    # 2
            "Definirla camera è un complimento: sporca, letto sfondato, cuscini inesistenti, finestra che non si chiude.",    # 1
            "Persiane rotte e arredi cadenti, per non parlare del bagno: doccia inesistente e sporcizia ovunque.",            # 1
            "Hotel pessimo/penoso, stanze orribili/terribili, ogni cosa lì dentro sembra sporca.",                            # 4 -> 130
            "Le stanze sono piccole e brutte, le pareti e il soffitto sarebbero da risistemare/reimbiancare!",                # 2            
            "Gli insetti ti tengono compagnia tutta/durante la notte e il bagno non è commentabile!",                         # 2
            "Un bagno in tale stato (doccia pietosa), che fa venir voglia piuttosto di non lavarsi!",                         # 1
            "Moquette che non vede aspirapolvere da anni, finestre che non si chiudono, pulizia zero, muffa alle pareti.",    # 1
            "Tv rotte, camere spoglie e atmosfera triste e cupa. Siamo scappati/fuggiti via!",                                # 2
            "Camere non proprio pulitissime come tutto lo stato dell'hotel del resto.",                                       # 1
            "Bagno sprovvisto di phon, sapone e asciugamani. Acqua calda in realtà solo tiepida.",                            # 1
            "Situazione pulizia gravissima! Segnalato più volte, nessun cambiamento. Da evitare!",                            # 1
            "Lavandino nel bagno otturato/intasato; struttura fatiscente piena di polvere.",                                  # 2
            "Tappeto con enormi/grandi macchie, parete rotta e un bagno inquetante... Hotel da incubo.",                      # 2
            "Lasciate fuori ogni speranza. Albergo brutto, stanze pessime e sporche.",                                        # 1
            "Maniglia rotta, la porta non si può chiudere se non direttamente a chiave. Arredi vecchi e trascurati.",         # 1
            "Bagno puzzolente, non lavato da chissà quanto. Luce dello specchio con almeno tre dita di polvere.",             # 1
            "Doccia spaventosa/terribile, tendina rotta che non sta su. Filtro dell'aria intasato di polvere.",               # 2 -> 150
            "Piumone e lenzuola con delle macchie. Peli di altri clienti nel letto. Crepe sui muri.",                         # 1
            "Camere e tutta la struttura da rivedere/controllare. Non terribile ma molto trascurato.",                        # 2
            "Albergo sporco, fatiscente, coperte macchiate di urina e chissà che cos'altro.",                                 # 1
            "Polvere/sporcizia ovunque, moquette sporca/sozza, letto sfondato/malconcio.",                                    # 8
            "Finestre della camera rotte/guaste e impossibili da chiudere/sigillare, arredi vecchi e rotti.",                 # 4
            "TV e wifi fuori uso. Arredi vecchi, aria condizionata non funzionante.",                                         # 1
            "Uno schifo simile non l'ho mai visto. Vacanza squallida per colpa dell'albergo.",                                # 1
            "Dire che fa pena è fargli un complimento! Struttura squallida/desolata e vecchissima.",                          # 2
            "La camera è da film horror. Fuggite finchè siete in tempo.",                                                     # 1
            "Finestre che non servono a niente, ci sono spifferi e si sente ogni rumore/suono esterno.",                      # 2
            "Il bagno cade a pezzi, lo sciacquone/scarico non è funzionante, la doccia quasi fredda e non regolabile.",       # 2
            "Stanza freddissima! Termosifoni spenti/chiusi il 31 dicembre.",                                                  # 1
            "Moquette e tappeti macchiati ovunque. Muri neri di polvere. Evitate questa struttura/sistemazione.",             # 2
            "Un vero e proprio incubo. Dovevamo restare 2 giorni diventati poi 1 per lo schifo nella stanza.",                # 1
            "Bagni pessimi, diroccati distrutti e sporchi, puzza di polvere ovunque.",                                        # 1
            "Moquette sporca, macchiata, bucata, bruciata, e impolverata. Muri crepati e cadenti.",                           # 1
            "Doghe/assi rotte nel letto, termosifone non funzionante, finestre con spifferi in ogni angolo.",                 # 2
            "L'esperienza peggiore che ci sia mai capitata. Non funziona niente e sporco ovunque.",                           # 1
            "Struttura vecchia/antiquata, per non parlare della camera sporca.",                                              # 2
            "Pulizia zero/inesistente nel bagno.",                                                                            # 2
            "Terribili le condizioni in cui versa; moquette nera (in origine era rossa ed a fiori), camera maleodorante.",    # 1
            "Struttura vecchia e camera piena di crepe che dà l'impressione possa crollare da un momento all'altro!",         # 1
            "Coperte macchiate/sporche e polvere ovunque. Camera rumorosa e poco attrattiva.",                                # 2
            "La struttura/camera lascia molto a desiderare: sporca e trascurata.",                                            # 2
            "Camera brutta vecchia e sporca, ma il pezzo forte è il bagno, scomodo e indecente è dir poco!",                  # 1
            "Esperienza davvero pessima. Scale, corridoi, stanze, sono rivestite di moquette consumata e impolverata.",       # 1
            "Il letto puzzava di polvere/stantio, la tv non trasmetteva nessun canale/segnale.",                              # 2
            "Bagno terribile, stretto/angusto, per nulla funzionale e con molti accessori fuori uso.",                        # 2 -> 200
            "Atmosfera e ambiente cupi e tristi. Tutto vecchio o guasto.",                                                    # 1
            "Sporco e freddo, non ci ritornerò.",                                                                             # 1
            "Le camere cadono a pezzi e la pulizia non è eccellente/ottimale.",                                               # 2
            "Niente wifi, niente aria condizionata, poca pulizia e servizi inesistenti.",                                     # 1
            "Avremmo preferito non trovare i boxer di qualcun altro accanto al letto. Devo continuare?",                      # 1
            "Edificio datato e interni trasandati con ovunque una sudicia moquette.",                                         # 1
            "Copriletto lercio, porte rattoppate e malconce, doccia, priva di piatto, adiacente al wc (doppio uso?).",        # 1
            "Non consiglio a nessuno questo albergo. Sudiciume e strafottenza/menefreghismo ovunque.",                        # 2
            "Stanza piccolissima e poco pulita. 0/nessun comfort.",                                                           # 2
            "Aria condizionata a malapena funzionante, wifi inesistente.",                                                    # 1
            "Le pareti sono sottilissime e si sente molto rumore/caos dalle altre camere.",                                   # 2
            "L'hotel è vecchio e logoro e poco curato. La pittura completamente scrostata dalle pareti.",                     # 1
            "Macchie sulle lenzuola e aria condizionata non funzionante. Non ci ritornerei.",                                 # 1
            "Bagno con doccia senza saliscendi e senza bidet, assenza di asciugacapelli.",                                    # 1
            "Igiene scarsa, per non parlare della moquet d'annata non adeguatamente pulita.",                                 # 1
            "Stanza logora, moquette bisunta, bagno troppo piccolo con odore tremendo/orrendo.",                              # 2
            "Camera in stato miserevole e odore pungente in ogni ambiente.",                                                  # 1
            "Uno dei letti era rotto, condizionatore d'aria vecchio e rumoroso, non abbiamo avuto acqua calda.",              # 1
            "L'hotel è datato, vetusto. Avrebbe bisogno di un rinnovamento totale.",                                          # 1
            "È un posto che sconsiglio vivamente! Ai limiti della decenza per camere, bagno, pulizie... Non andateci!",       # 1
            "Le camere avrebbero bisogno di maggiori cure e manutenzione.",                                                   # 1
            "Albergo molto vecchio e malconcio. Camere cupe e asfissianti senza nessun comfort.",                             # 1
            "Camere vecchie e sudicie. Esperienza tristissima/bruttissima da non ripetere.",                                  # 2
            "Bagno sporco al limite della decenza, senza acqua calda né phon.",                                               # 1
            "Letto scomodo e cuscini così sottili da essere inutili. Pulizia approssimativa.",                                # 1
            "Camere poco confortevoli, poco curate e poco pulite.",                                                           # 1
            "Bagno piccolissimo/strettissimo, disfunzionale e anche molto/parecchio sporco.",                                 # 4
            "Hotel da evitare; condizioni della struttura pessime. Ogni cosa o è vecchia o è rotta!",                         # 1
            "Delusione/Amarezza e rimpianto. Albergo/Alloggio vecchio e sporco.",                                             # 4
            "Muffa alle pareti e sporcizia, copriletti strappati e ricuciti, termosifoni inesistenti, doccia senza box.",     # 1
            "Se volete alloggiare/pernottare in questo hotel, dimenticate/scordate la pulizia e la comodità.",                # 4
            "Il rubinetto che perde e il condizionatore rumoroso non ci hanno fatto chiudere occhio.",                        # 1
            "Camera al 4° piano e ascensore fuori servizio/uso per tutta la durata del soggiorno.",                           # 2
            "Cattivi odori persistenti, sporco ostinato in zone difficili (fughe delle piastrelle, angoli, tendine doccia).", # 1 -> 250
            "Dotazioni mancanti o obsolete: assenza di elementi/gadget standard.",                                            # 2
            "Arredi vecchi e usurati, mancanza di pulizie extra e cambi di biancheria/lenzuola.",                             # 2
            "Stanze rumorose o con problemi di isolamento acustico, scarsa illuminazione e ventilazione.",                    # 1
            "Sensazione di abbandono ovunque: muri sporchi e macchiati, pareti non imbiancate, aree comuni trascurate.",      # 1 = 139 -> 256
            "Non ho potuto fare doccia per tre giorni, era veramente disgustosa!",                                            # 1
            "La descrizione della struttura non corrisponde; è tutto diverso (in peggio) dalle foto.",                        # 1
            "Chiamarlo topaia é un complimento! Camera minuscola e sporca (piena di capelli e peli ovunque).",                # 1
            "Ambiente sporco, mobilia vecchia. Camere molto molto piccole.",                                                  # 1
            "La camera dispone di un wc/water/gabinetto rotto e la doccia e aria condizionata non funzionano.",               # 3
            "Abbiamo trovato un cerotto usato nel letto. Raccapricciante!"                                                    # 1 = 144 -> 264
        ]
    },
    'Reception': {
        'pos': [
            "Check-in rapido/veloce e personale molto accogliente/cordiale.",                                                          # 4
            "Reception efficiente/funzionale e disponibile; risolvono qualsiasi problema/situazione in pochissimo tempo.",             # 4
            "Staff/personale cordiale e professionale al banco/desk; servizi di prima/ottima qualità.",                                # 8
            "Servizi e personale/addetti TOP. Consigliatissimo.",                                                                      # 2
            "Un soggiorno davvero piacevole. Comodo, con parcheggio custodito e tante attenzioni rivolte al cliente.",                 # 1
            "Personale disponibile e cordiale. Ascensore. Parcheggio e tanti servizi.",                                                # 1
            "Ho trovato il personale molto disponibile e pronto a soddisfare tutte le richieste che gli facevamo. Consigliato.",       # 1
            "Grande cortesia/simpatia e gentilezza del titolare e di tutti gli addetti.",                                              # 2
            "Accoglienza splendida. Nonostante alcune difficoltà che il personale ha prontamente risolto siamo stati benissimo.",      # 1
            "Hotel molto bello e confortevole/accogliente, personale sempre disponibile e gentile.",                                   # 2
            "Siamo rimasti colpiti positivamente da questa struttura; il personale è accogliente e sempre disponibile.",               # 1
            "In questo hotel mi trovo come a casa, piena efficenza e disponibilità. Cortesia e Servizio ottimi/stupendi.",             # 2
            "Questo albergo/hotel è UNA MERAVIGLIOSA CERTEZZA grazie a tutto lo staff.",                                               # 2
            "Finezza ed eleganza. Siamo rimasti colpiti positivamente da questa struttura e dal personale che ci lavora.",             # 1
            "Personale squisito, hotel piccolo ma ottimo e molto confortevole.",                                                       # 1
            "Accoglienza ottima e il personale carismatico. Hanno risposto a tutte le nostre domande/richieste.",                      # 2
            "Ogni cliente/ospite è accolto con il massimo delle attenzioni.",                                                          # 2
            "Personale sempre disponibile e tanti servizi inclusi/compresi nel prezzo.",                                               # 2
            "Cordialità e disponibilità del personale e della direzione, mi hanno risolto ogni problema/complicazione/incombenza.",    # 3
            "L'albergo offre un servizio di lusso ad un prezzo decisamente contenuto.",                                                # 1
            "La prima cosa che colpisce entrando/arrivando è la cordialità del personale.",                                            # 2
            "Il personale della reception/struttura si prodiga/impegna per soddisfare qualsiasi richiesta.",                           # 4
            "La struttura mette a disposizione dei clienti un bus-navetta gratuito per andare ovunque si desideri.",                   # 1
            "Il personale è molto cordiale e molto preparato sulle lingue straniere.",                                                 # 1
            "Con disponibilità e professionalità, il personale e la direzione vi coccolano come se foste a casa vostra.",              # 1
            "Ottimo staff e personale alla reception sempre presente e sempre disponibile.",                                           # 1
            "La cosa migliore dell'albergo è sicuramente il personale, tutti molto gentili e simpatici.",                              # 1 -> 50
            "Check-in rapido/veloce ed efficiente. Dopo 2 minuti dall'arrivo eravamo già in camera.",                                  # 2
            "Fin dall'accoglienza alla reception, siamo stati accolti da un personale incredibilmente cordiale",                       # 1
            "Personale dell'hotel professionale e sempre pronto ad aiutare.",                                                          # 1
            "Staff: Cordialità, efficienza, disponibilità e professionalità.",                                                         # 1
            "Reception aperta anche di notte, gentilezza massima, late check out, frigo bar e ottima zona/posizione.",                 # 2
            "Hotel molto confortevole, addetti/dipendenti cordiali e disponibili.",                                                    # 2
            "Grande professionalità del personale che rende questo Hotel eccellente!",                                                 # 1
            "Una bella esperienza in termini di accoglienza, cordialità, attenzione al cliente e comodità",                            # 1
            "Hotel ricco di semplici/piccoli dettagli che rendono la massima soddisfazione al tuo soggiorno/pernottamento.",           # 2
            "Struttura comoda e con personale cortese e disponibile. Ottimo per un viaggio di lavoro/relax.",                          # 2
            "Personale cordiale, preparato e che conosce le lingue!",                                                                  # 1
            "Gentilezza e disponibilità dello staff, posizione strategica e tranquillità/relax. Consigliato.",                         # 2
            "La permanenza è stata eccezionale! Dalla calorosa accoglienza al check-out, tutto è stato gestito con cura/attenzione",   # 2
            "Lo staff è stato sempre gentile e cordiale facendoci sentire come a casa nostra.",                                        # 1
            "Un plauso speciale/particolare al team della reception. Tutto è stato gestito con velocità e con cura.",                  # 2
            "Gli addetti alla reception sono stati incredibilmente professionali e rapidi nel risolvere un errore di prenotazione.",   # 1
            "Nel giro di 10 minuti dall'arrivo avevamo le chiavi della nostra camera, senza stress e con un sorriso",                  # 1
            "Un servizio clienti di questo livello fa davvero la differenza. Grazie!",                                                 # 1
            "L'sperienza in questo hotel è stata ottima fin dal momento del check-in: veloce ed efficiente.",                          # 1
            "Alla reception sono stati gentilissimi, ci hanno offerto subito una bottiglia d'acqua fresca e una mappa della città.",   # 1
            "Alla reception ci sono stati consigliati tutti i migliori posti della città da visitare/esplorare. Promosso.",            # 2
            "Un punto di forza assoluto/totale di questo hotel è la competenza/preparazione del personale al desk.",                   # 4
            "Ogni nostra domanda è stata risposta con pazienza e grande conoscenza della zona. Servizio a 5 stelle!",                  # 1 
            "Abbiamo chiesto indicazioni alla reception su come muoverci in città e siamo stati assistiti in tutto e per tutto.",      # 1
            "Alla reception forniscono in automatico una mappa/cartina della città e l'orario dei mezzi pubblici.",                    # 2
            "Check-in e servizi impeccabili: tutto gestito alla perfezione.",                                                          # 1
            "Ho contattato la reception via email e si sono occupati di tutto con la massima professionalità/disponibilità.",          # 2
            "L'efficienza del servizio concierge è stata notevole/ragguardevole.",                                                     # 2
            "Anche il check-out, richiesto in anticipo alle 6:00 del mattino, è stato gestito senza intoppi e con grande puntualità.", # 1
            "Un'esperienza senza stress. Il personale dell'hotel fornisce aiuto e assistenza per qualsiasi richiesta.",                # 1
            "Un plauso all'efficienza della reception 24 ore su 24.",                                                                  # 1
            "Il personale ha gestito/risolto ogni nostro problema con grande rapidità e gentilezza.",                                  # 2
            "Ci hanno prenotato i biglietti per il museo/teatro e dato ottimi consigli sui tour dei locali della zona",                # 2 -> 100
            "Procedure veloci e senza attese. Check-out espresso gestito perfettamente.",                                              # 1
            "La chiave/tessera magnetica era guasta ma il problema è stato risolto in 1 minuto! Ottima efficienza.",                   # 2
            "Grazie all'ottimo personale che parlava bene/fluentemente inglese, non c'è stata alcuna barriera linguistica.",           # 2
            "È stato rassicurante sapere che c'era sempre qualcuno al desk anche alle 3 del mattino.",                                 # 1
            "Hanno organizzato il nostro taxi per l'aeroporto in 5 minuti. Servizio sveglia affidabile e preciso/puntuale.",           # 2
            "Ci hanno tenuto le valigie per tutto il giorno anche dopo il check-out. Gentilissimi.",                                   # 1
            "Camera pronta già all'arrivo e bagagli portati su in camera in un attimo.",                                               # 1
            "L'area della reception/hall era pulita e accogliente. Personale sempre sorridente e pronto ad aiutare.",                  # 2
            "Flessibilità e supporto/assistenza post check-out impeccabili/impareggiabili.",                                           # 4
            "La reception ha gestito il deposito dei nostri bagagli senza alcun costo aggiuntivo/ulteriore anche dopo il check-out.",  # 2
            "Il servizio, gestito interamente dal personale del front desk, mostra una grande attenzione per il cliente.",             # 1
            "L'albergo ha accettato di modificare le date senza penali, riassicurandomi che non ci sarebbero stati problemi.",         # 1
            "La disponibilità del personale a venire incontro alle nostre esigenze/necessità è stata molto apprezzata.",               # 2
            "Un ringraziamento speciale al team della reception/concierge per aver reso il nostro viaggio indimenticabile.",           # 2
            "Affidarsi ai consigli/suggerimenti del personale dell'hotel è stato il valore aggiunto della nostra vacanza.",            # 2
            "La risposta della reception a tutte le mie richieste è sempre arrivata entro poco tempo, chiara e professionale.",        # 2
            "Ottima efficienza nella comunicazione pre e post soggiorno/vacanza/pernottamento.",                                       # 3
            "Il check-in è durato meno di due minuti, un record! Personale attento e preparato.",                                      # 1
            "Ottimo parcheggio privato/riservato, custodito e disponibile a qualunque ora per noi ospiti della struttura.",            # 2
            "Assistenza tecnica rapida ed efficace, gestita direttamente dal personale del front desk. Ottimo servizio.",              # 1
            "Massima sicurezza all'interno della struttura e controllo accessi efficiente/scrupoloso.",                                # 2
            "Servizio di vigilanza privata all'esterno della struttura. Ottimo per sentirsi sicuri/protetti.",                         # 2
            "La reception monitora costantemente gli accessi e si assicura che solo gli ospiti registrati entrino.",                   # 1 
            "Poichè era il nostro anniversario, alla reception, oltre agli auguri, ci è stato offerto dello champagne!",               # 1
            "A causa di un piccolo disguido, la nostra camera è stata sostituita/rimpiazzata da una suite senza nessun aggravio!",     # 2
            "La capacità della reception di personalizzare l'esperienza è stata la ciliegina sulla torta della nostra vacanza.",       # 1
            "Ci sono state fornite indicazioni precise su orari di treni, bus per l'aeroporto, e noleggio auto. TOP.",                 # 1
            "Il gestore è stato ottimo per disponibilità, gentilezza e preziosi consigli su cosa visitare e dove mangiare in città.",  # 1
            "L'albergo offre tutto ciò di cui potresti avere bisogno. Gestore/host molto cordiale e simpatico.",                       # 2
            "La struttura ha fornito molte informazioni utili per il nostro soggiorno e ha risposto a tutte le nostre domande.",       # 1
            "Il proprietario è un gestore gentilissimo e preparato, ti spiega tutto nel dettaglio ed è estremamente disponibile.",     # 1
            "Host eccezionale, disponibile, gentile e super/molto attento a qualsiasi esigenza/necessità.",                            # 4
            "Personale molto disponibile/attento a tutte le ore e per qualsiasi informazione/evenienza.",                              # 4
            "Il personale è gentilissimo e dà ottimi consigli su dove mangiare/pranzare, cosa visitare e come muoversi.",              # 2 -> 150
            "Siamo arrivate dopo mezzanotte e non c'è stato alcun problema per poter accedere sia all'albergo che alla camera.",       # 1
            "Albergo molto funzionale pieno di servizi. Dipendenti simpatici e sempre disponibili/pronti.",                            # 2
            "Host insuperabile per cortesia (sin dalla fase di prenotazione), organizzazione della struttura e disponibilità.",        # 1
            "Grazie di cuore! E' stato bello conoscervi.",                                                                             # 1
            "Accoglienza familiare. Il gestore, che ringraziamo ancora, con i suoi suggerimenti, è stato un valore aggiunto.",         # 1
            "Personale stupendo, sempre disponibile per ogni esigenza. Consigliato/suggerito/raccomandato.",                           # 3
            "Il personale è stato molto utile con tutto, dal lasciare i bagagli alle raccomandazioni sui ristoranti.",                 # 1
            "Il gestore è stato incredibilmente disponibile per qualsiasi esigenza. Ci tornerei sicuramente.",                         # 1
            "Staff molto disponibile e preciso nell'indicare cosa visitare e dove andare per una cena o un aperitivo.",                # 1
            "Il personale è stato veramente gentile ed accomodante, sempre disponibile per qualsiasi necessità.",                      # 1
            "Grazie ai ragazzi della reception e del servizio ai piani per l'ottima accoglienza/ospitalità.",                          # 2
            "Dipendenti molto disponibili a fornire consigli su ristoranti, noleggio auto e altro.",                                   # 1
            "Personale molto preciso e disponibile nel fornirci indicazioni e suggerimenti su trasferimenti da e per l'aeroporto.",    # 1
            "Soggiorno fantastico; struttura nuova e ben/ottimamente gestita.",                                                        # 2
            "Proprietario gentilissimo, super disponibile. Offre tantissimi servizi senza far pagare 1 euro in più!",                  # 1
            "Lo staff al desk ti aiuta con qualsiasi incombenza da sbrigare, dal chiamare un taxi al prenotare una visita guidata.",   # 1
            "Gestione formidabile/impeccabile: personale preciso, puntuale, serio e molto disponibile.",                               # 2
            "La reception dispensa consigli su come muoverti, cosa visitare, dove mangiare e tutto ciò che riguarda la città.",        # 1
            "Personale sempre attento che tutto sia perfetto. Proprietari gentilissimi e simpatici.",                                  # 1
            "Host straordinario: disponibile, cortese e sempre pronto ad aiutare sia prima che durante il soggiorno.",                 # 1
            "L'attenzione ai particolari e la dedizione verso gli ospiti fanno davvero la differenza in questo b&b/agriturismo.",      # 2
            "Complimenti vivissimi/sentiti al proprietario per la sua professionalità e passione.",                                    # 2
            "Soggiorno piacevolissimo in questa struttura grazie alle mille e una attenzione che hanno avuto per noi.",                # 2
            "Il personale riesce con professionalità a risolvere qualsiasi problema/necessità in pochissimo tempo.",                   # 2
            "Hall affascinante e arredata con molto buon gusto. Personale incantevole.",                                               # 1
            "Il proprietario è persona di una cortesia unica, sempre disponibile ad elargire consigli per un piacevole soggiorno.",    # 1
            "Il proprietario è molto attento e cortese, più che ottimo il rapporto qualità-prezzo vista la posizione del B&B.",        # 1
            "Il responsabile è stato molto gentile e attento per tutto il tempo/soggiorno. Ci ha sollevato da molte incombenze.",      # 2
            "Gestore disponibile e preparato che ci ha aiutato molto nell'organizzazione.",                                            # 1
            "Il personale ci ha dato ottimi consigli per ristoranti ed escursioni; albergo molto consigliato.",                        # 1
            "Il personale è andato oltre le nostre aspettative per assicurarsi che il nostro soggiorno fosse perfetto.",               # 1
            "Host squisito, fornisce tutte le informazioni/indicazioni utili ed è a vostra disposizione prima e durante il soggiorno.",# 2
            "Qualsiasi quesito/problema abbiate, il desk è sempre pronto a fornirvi la soluzione ottimale/perfetta.",                  # 4
            "Un plauso al gestore/direttore della struttura, super gentile, disponibile e presente per ogni evenienza.",               # 2 -> 200
            "Eccellente/ottimo servizio clienti. Altamente raccomandato/consigliato!",                                                 # 4
            "Grazie al direttore e al suo staff per la professionalità e la simpatia.",                                                # 1
            "Staff reattivo e disponibile per ogni emergenza/evenienza. Moltissimi/tantissimi servizi inclusi nel prezzo.",            # 4
            "La cortesia, la gentilezza e la preparazione dello staff hanno reso il nostro soggiorno ancora più piacevole.",           # 1
            "Ho viaggiato centinaia di volte e non ho mai visto/trovato un ospite così disponibile e amichevole come qui.",            # 2
            "Non dimenticherò mai il gesto che hai fatto affinché potessimo fare colazione sul balcone. Grazie mille per tutto.",      # 1
            "Il desk ci ha fornito ottimi consigli per parcheggiare, per mangiare, ma anche per le nostre visite guidate/culturali.",  # 2
            "Check-in facile/semplice e tanti consigli super graditi per visitare luoghi di interesse e per mangiare ottimamente.",    # 2
            "Personale accogliente, disponibile, premuroso e sensibile. Spero di tornarci il prima possibile.",                        # 1
            "I proprietari sono molto attenti ad ogni dettaglio. Ti assistono in tutto e sono pronti nel risolvere ogni problema.",    # 1
            "Accoglienza perfetta/stupenda, sempre disponibili per ogni esigenza che possa presentarsi/manifestarsi.",                 # 4
            "Nessun problema o ritardo nelle procedure/adempienze. Tutto è tato gestito con rapidità/velocità ed efficienza.",         # 4
            "Ho dovuto cambiare/modificare la prenotazione 2 volte e non mi è stato fatto alcun problema dall'hotel.",                 # 2
            "L'albergo ha accolto tutte le nostre richieste/esigenze speciali senza alcuna problematica/rimostranza.",                 # 4
            "Ascensori e tutti i servizi sempre funzionanti. Reception sempre pronta/attenta.",                                        # 2
            "Ci sono state date tutte le informazioni con chiarezza, disponibilità e cortesia dal personale.",                         # 1
            "La cura e la passione che i propietrari mettono nel gestire il b&b, fanno sentire l'ospite a casa.",                      # 1
            "Parcheggio disponibile e gratuito in hotel. Prenotazione tramite il sito istituzionale dell’hotel semplice e sicura.",    # 1
            "Ho trascorso tre giorni di relax, coccolata/servita da personale davvero professionale e sempre disponibile.",            # 2
            "ho apprezzato molto la disponibilità del personale, sempre pronto nel venire incontro alle esigenza degli ospiti",        # 1            
            "Ottimo servizio con aperitivo di benvenuto; receptionist sempre gentili e disponibili.",                                  # 1
            "Aperitivo di benvenuto e kit di cortesia in tutte le camere. Ottimo albergo per essere coccolati.",                       # 1
            "L'hotel offre anche delle navette gratuite per raggiungere le località/zone vicine. Promosso.",                           # 2
            "Magnifico staff che ti accoglie per tutto ciò di cui hai bisogno. Ottimo il personale del ristorante e della reception.", # 1
            "Staff efficientissimo, molto presente e preparato anche sui consigli per i posti da visitare/vedere.",                    # 2
            "Il servizio di ricevimento ospiti è pilastro portante della struttura. Professionalità e disponibilità massime.",         # 1
            "Complimenti soprattutto al personale di sala e reception, gentili e sempre con un occhio di riguardo verso gli ospiti.",  # 1 -> 250
            "Servizi impeccabili e personale preparato, gentile e disponibile.",                                                       # 1
            "In albergo è presente anche un centro benessere/salute totalmente/completamente gratuito e molto confortevole.",          # 4
            "SPA interna molto pulita e molto ben gestita dallo staff.",                                                               # 1
            "Apprezzo/Ammiro molto l'eccellente/ottimo servizio clienti e l'attenzione ai dettagli/particolari.",                      # 8 = 158 -> 264
            "Ottimi servizi in camera offerti dalla reception: kit di benvenuto e una bottiglia omaggio.",
            "L'albergo ha svolto un servizio di check-in in camera molto comodo e professionale.",
            "Kit di cortesia disponibile in tutte le camere e per ogni ospite."
        ],
        'neg': [
            "Check-in lento e disorganizzato.",                                                                                        # 1
            "Personale della reception scortese e poco disponibile.",                                                                  # 1 
            "Attesa lunga/snervante alla registrazione e poca chiarezza/trasparenza nelle informazioni.",                              # 4
            "A causa di un guasto è mancata l'acqua calda in camera per tutto il soggiorno/periodo.",                                  # 2
            "Ascensore non funzionante per una settimana.",                                                                            # 1
            "Nessuno alla reception e nessuno al bar che era chiuso e inaccessibile.",                                                 # 1
            "Il mio numero di telefono trascritto sbagliato e le mie email finite nello spam! Pessimo servizio.",                      # 1
            "Personale scortese che mette ansia. Qualsiasi/ogni richiesta extra viene respinta a priori.",                             # 2
            "Molto delusa! Non hanno accettato un cambio di prenotazione né fornito alcun rimborso/indennizzo.",                       # 2
            "Non hanno nemmeno la decenza/dignità di trattare bene i pochi clienti/ospiti che hanno sono senza parole.",               # 4
            "Addetti/Responsabili notturni alla reception davvero incapaci/incompetenti e svogliati.",                                 # 4
            "Non particolarmente accogliente/ospitale. Personale svogliato se non addirittura maleducato/sgarbato.",                   # 4
            "Ho dovuto chiedere/chiamare più volte per poter avere una coperta in più e per sapere come attivare il wifi.",            # 2
            "Alla reception non ti danno alcuna informazione/indicazione e in camera non funziona quasi nulla/niente.",                # 4
            "Il proprietario continuava a tormentarci, bussava alla porta della nostra camera al mattino e cercava di entrare.",       # 1
            "Avevo prenotato con ingresso alle 13:00, ma quando siamo arrivati non c'era nessuno ad aspettarci/attenderci.",           # 2
            "Accetta/Prende prenotazioni anche se non ha posti letto, dirottando su un altro albergo pessimo/orribile.",               # 1                     
            "Le camere risultano libere anche quando in realtà sono occupate/impegnate.",                                              # 2
            "Se vi lamentate della sistemazione iniziano ad urlare e a chiamarvi ladri. Da evitare come la peste.",                    # 1
            "Nessuno tra il personale alla reception parlava la nostra lingua.",                                                       # 1
            "Non c'è una reception o qualcosa di simile e quindi non si ha la possibilità di contattare nessuno.",                     # 1
            "Scarsa trasparenza e poca chiarezza su politiche di cancellazione, rimborsi e depositi.",                                 # 1
            "Problemi con la gestione di documenti o identificazioni (richiesta di documenti non chiara e eccessiva).",                # 1
            "Bisognerebbe ristrutturare la hall e assumere uno staff più cordiale/gentile.",                                           # 2
            "Nessuna accoglienza, nessuno che ti accompagni in un labirinto di scale pianerottoli fino alla tua camera.",              # 1 -> 50
            "In ascensore entrano a malapena/stento 2 persone senza valige/bagagli.",                                                  # 4
            "Personale poco gentile e frettoloso/superficiale in ogni occasione/situazione/circostanza.",                              # 6
            "Il personale delle pulizie inizia a disturbare/infastidire già alle 7:30 bussando per essere aperti.",                    # 2
            "Reception aperta solo poche ore al giorno. Nessun/niente personale durante la notte.",                                    # 2
            "Difficile/complicato/arduo trovare la camera con le scarse e scarne informazioni/indicazioni fornite.",                   # 6
            "Carenza cronica/costante di personale. Non c'è mai nessuno/qualcuno a cui chiedere informazioni.",                        # 4
            "Servizio lento, brusco e generalmente negativo. Pochi impiegati e spesso impreparati/inesperto.",                         # 2
            "Cordialità/Gentilezza di tutto personale: zero assoluto. Non ci tornerò mai più.",                                        # 2
            "C'era qualcuno al mio piano che durante la notte ha iniziato a urlare/gridare piú volte svegliando tutti.",               # 2
            "Il check-in più disorganizzato/caotico mai visto. Hanno sbagliato 3 volte a scrivere/compilare i miei dati.",             # 4
            "Lo staff ha risposto male e sempre negativamente a qualsiasi richiesta/domanda.",                                         # 2
            "Personale non accogliente e poco disponibile.",                                                                           # 1
            "La reception non è all'interno dell'hotel, quindi se vuoi chiedere/avere informazioni devi prenderti la pioggia",         # 2
            "Niente telefono in camera; per contattare/chiamare la reception devi usare il tuo telefono.",                             # 2
            "Niente acqua calda, solo tiepida, che in inverno è inaccettabile/inammissibile.",                                         # 2
            "Il portiere/custode di notte ci ha rivelato che il riscaldamento è guasto/rotto da 8 anni.",                              # 4
            "Il personale dell'hotel ha fatto sparire alcuni miei effetti personali. Ho sporto denuncia.",                             # 1
            "Siamo giunte/arrivate di mattina (così come da prenotazione) ma la nostra camera è stata liberata solo di pomeriggio.",   # 2 -> 100
            "Servizio sia ai piani che alla reception veramente/davvero scarso. Albergo da massimo 1 stella.",                         # 2
            "Il personale della reception dovrebbe prestare più attenzione alle esigenze/richieste/necessità dei clienti.",            # 3
            "Personale maleducato/rozzo e addetti al facchinaggio senza alcuna cura/attenzione per i nostri bagagli.",                 # 4
            "Gente che si asciuga i capelli di notte, sbatte le porte, musica ad alto volume, sconsigliatissimo.",                     # 1
            "La cameriera si è messa a gridare/urlare perché mia moglie ha chiesto se poteva avere un té.",                            # 2
            "Il personale sembra sempre che ti stia facendo un favore per qualsiasi richiesta/cosa.",                                  # 2
            "Ho chiesto se potevano chiamarmi un taxi e mi è stato risposto che potevo chiamarmelo da solo.",                          # 1
            "Abbiamo attesto/aspettato oltre mezz'ora alla reception che arrivasse un addetto per il check-in.",                       # 2
            "Addetto alla reception per niente professionale, non indossava nemmeno l'uniforme.",                                      # 1
            "Ad ogni segnalazione, il personale risponde con un sorriso e una promessa ma poi di fatto non fa nulla.",                 # 1
            "Personale poco disponibile e schietto fino alla maleducazione/scortesia.",                                                # 4                     
            "Accoglienza quasi zero/nulla e senza ascensore (4 piani!).",                                                              # 2
            "Gente che entra ed esce dall'albergo poco raccomandabile...",                                                             # 1
            "Fin dalla prenotazione, ho parlato con personale scortese a livelli esagerati/estremi.",                                  # 2
            "OVERBOOKING a mezzanotte; nonostante prenotazione non avevano riservato/tenuto una stanza per me.",                       # 2
            "Prenotato online e pagato in anticipo, quando sono arrivato ho scoperto che non avevano camere.",                         # 1
            "Il comportamento/contegno del personale dell'hotel è pessimo. Maleducati e cafoni.",                                      # 2
            "Alla reception un confuso/disordinato signore ha impiegato 10 minuti per trovare la mia prenotazione.",                   # 2
            "La correttezza e la professionalità non sono di casa in questo porcile chiamato hotel.",                                  # 1
            "Ci hanno costretto a cambiare camera da un giorno all'altro senza darci spiegazioni e con molto disagio/fastidio.",       # 2
            "Avevamo una camera con bagno ma dopo un giorno ci hanno spostato in una camera senza bagno senza preavviso. Servizio clienti deludente",   # 1
            "Personale impreparato/incapace che ha creato disordine e confusione per il pagamento.",                                   # 1
            "Il personale non comprende l'italiano e quando lo capivano erano TOTALMENTE DSINTERESSATI a qualsiasi richiesta.",        # 1
            "Quando ho fatto notare/rilevare che dalla finestra entrava acqua mi è stato risposto e quindi cosa vuoi?",                # 2
            "Reception praticamente inesistente/immaginaria: 0 personale, 0 servizi, 0 professionalità.",                              # 2
            "All'arrivo in hotel ci sono stati richiesti ulteriori soldi (non previsti) per darci la camera già pagata.",              # 1
            "Il receptionist ci ha accolti con le pantofole e nonostante stessimo a Milano non parlava italiano!",                     # 1            
            "Per uscire alle 7, abbiamo dovuto svegliare il tipo della reception che si è presentato in pigiama e infradito.",         # 1
            "In fase di check-in ci hanno chiesto di pagare 40 euro per avere elettricità/corrente in camera. Da denuncia.",           # 2 -> 150
            "Pieno di tariffe nascoste/occultate. Il soggiorno mi è costato 100 euro in più al giorno. Ladri/truffatori.",             # 4
            "Nonostante le nostre rimostranze/proteste/lamentele non è stato possibile aver alcun supporto/aiuto dal personale.",      # 6          
            "Il personale si è rivelato impreparato, poco educato e menefreghista riguardo ad ogni situazione/circostanza.",           # 2
            "Receptionist talmente/così scortese che speravamo di non incontrarlo.",                                                   # 2
            "La risposta alle nostre lamentele è stata se non vi va bene andate in un altro albergo.",                                 # 1
            "Personale dell'hotel non professionale e pieno di pregiudizi sugli ospiti di colore.",                                    # 1
            "Albergo sprovvisto/privo di POS per pagare/saldare con carta o bankomat.",                                                # 4 
            "Durante la notte qualcuno ha cercato di entrare in camera nostra e non c'era alcun personale per segnalarlo.",            # 1
            "Alla reception non sono in grado di fornire/dare nessun aiuto né soluzione per nessun problema.",                         # 2
            "Prima mi hanno registrato e poi mi hanno comunicato/detto che la mia camera non aveva il bagno.",                         # 2
            "Albergo e personale pessimi/penosi. Scarsa sicurezza perfino all'interno delle camere. Estranei sul balcone.",            # 2
            "Non sono mai stata trattata così male come in questo albergo. Non ci ritornerò mai più.",                                 # 1
            "Ho avuto bisogno/necessità di effettuare check-in notturno ma mi è stato risposto che dovevo attendere la mattinna.",     # 2
            "Non metteteci piede, gente maleducata e comportamento/contegno pessimo.",                                                 # 2
            "Il personale ha spostato tutti i miei bagagli e gli effetti personali da una stanza all'altra senza dirmi nulla.",        # 1
            "Organizzazione scarsissima, i servizi non corrispondono a quello dichiarato dall'albergo.",                               # 1
            "Il soggiorno di relax programmato/prenotato in questo albergo è stato purtroppo deludente per molte ragioni.",            # 2
            "Dalla strada sottostante arriva/giunge nelle camere tantissimo rumore. Impossibile/impensabile riposare.",                # 4
            "Con grande stupore/incredulità, all'arrivo, ci è stato detto che l'albergo non accetta bambini.",                         # 2
            "Servizi pari a zero. Se pensate di andare in vacanza per rilassarvi/riposarvi questo non è per niente il posto adatto…",  # 2
            "Schiamazzi e persone che urlavano ia tutte le ore, sicuramente un comportamento non adatto/consono.",                     # 2
            "SPA inesistente anche se reclamizzata/pubblicizzata. Servizi scadenti e personale peggiore.",                             # 2
            "Pessimo trattamento/servizio da parte di tutto il personale. Non torneremo più.",                                         # 2 -> 200
            "Il ragazzo alla reception ci ha fatto salire e scendere 3 volte le scale prima di dirci come si accendeva la luce.",      # 1
            "È evidente che gli interessa solo il denaro e non certo la clientela. Cercate altre strutture per le vacanze.",           # 1
            "Il personale è maleducato e non sa gestire correttamente le richieste.",                                                  # 1
            "Per 5 minuti di ritardo ci hanno lasciato/chiusi fuori tutta la notte. Pessimi.",                                         # 2
            "Alla reception di quest'albergo solo strafottenza e arroganza.",                                                          # 1
            "File interminabili/infinite al check-in e un generale senso di abbandono/negligenza.",                                    # 2
            "Non hanno saputo darmi indicazioni sui mezzi pubblici (che ho dovuto chiedere al commesso del negozio a fianco).",        # 1
            "Il checkin è durato un'ora e mezza a causa del personale al desk che non sa fare il suo lavoro/mestiere.",                # 2
            "Tempi biblici/lunghissimi per la consegna delle chiavi dell'appartamento. Decisamente scortesi in reception.",            # 2           
            "Per nulla disponibili, scortesi e non rispettano gli orari. Vi consiglio di prenotare altrove.",                          # 1
            "Ogni volta che ho chiamato la reception per un problema/guasto, non hanno mai mandato nessuno a controllare.",            # 2
            "Condizioni di prenotazione non chiare/trasparenti, chiedono caparre/cauzioni non previste.",                              # 2
            "Totale scortesia del personale reception e totale inadeguatezza professionale.",                                          # 1
            "Gestione pessima. Scorrettezze ai limiti della truffa/denuncia.",                                                         # 2
            "Dopo aver acquistato e pagato la stanza mi hanno rifiutato il check-in quanto avrebbero voluto a garanzia 500 euro cash!",# 1
            "Il servizio e la modalitá di prenotazione sono pessimi.",                                                                 # 1
            "Consiglio ai gestori/proprietari dell'hotel più cordialità/gentilezza e meno arroganza.",                                 # 2
            "Non ho mai trovato personale così sgarbato, maleducato e insofferente come in questa struttura.",                         # 2
            "Scarsa disponibilità, e tanta tanta tanta SCORTESIA. In nessun posto al mondo mi é capitato di essere trattato così.",    # 1
            "Il tizio che accoglie gli ospiti non mette certamente le persone a proprio agio, sommario e poco professionale.",         # 1
            "Note negative: la mancanza di una reception, il personale dai modi decisamente sbrigativi.",                              # 1
            "Il parcheggio doveva essere gratuito e invece a fine soggiorno ci è stato fatturato/addebitato.",                         # 2
            "Il parcheggio interno/custodito era al completo e abbiamo dovuto lasciare l'auto in strada.",                             # 2
            "Il personale dell'albergo non ha saputo fornirmi indicazioni sui mezzi pubblici della zona.",                             # 1
            "La struttura non merita i soldi spesi.",                                                                                  # 1
            "Direzione poco professionale e poco accogliente nei confronti delle richieste dei clienti.",                              # 1
            "Mentre eravamo ancora in stanza per vestirci, sono entrati senza nemmeno bussare o avvisare.",                            # 1
            "Personale di sala scortese, mai un sorriso, piatti praticamente gettati sul tavolo, decisamente da migliorare.",          # 1
            "I camerieri non hanno la più pallida idea di come svolgere il loro lavoro/mestiere.",                                     # 1
            "Il personale non rispetta le minime norme/regole d'igiene.",                                                              # 2
            "Il portiere di notte fumava tranquillamente/beatamente nella hall dell'albergo, INAMMISSIBILE.",                          # 2
            "Se volevi dormire un po in più entrava la donna delle pulizie in camera intorno alle 8 senza bussare/chiedere.",          # 2             
            "Di notte, rumori forti e continui si propagano per tutta la struttura rendendo impossibile dormire/riposare.",            # 2
            "Hanno sbagliato le date di prenotazione del mio soggiorno e hanno anche fatto storie per modificarle.",                   # 1
            "Confusione su orari, servizi disponibili, tariffe e regole della struttura. Un vero caos questo posto.",                  # 1 -> 250
            "Al rientro/ritorno in camera la chiave/tessera di apertura non funzionava e non c'era nessuno ad aiutarci.",              # 4
            "Promesse non mantenute, risposte evasive o superficiali, mancanza di follow-up. Hotel da evitare/chiudere.",              # 2
            "Servizi aggiuntivi non disponibili/presenti o mal gestiti: nessun aiuto/supporto con i bagagli.",                         # 4
            "Percezione di scarsa sicurezza all'interno dell'albergo. Presenza di persone poco raccomandabili.",                       # 1
            "Servizio di noleggio auto gestito pessimamente/male dalla reception.",                                                    # 2
            "Esperienza pessima/negativa: in sauna mancava l'acqua calda.",                                                            # 2
            "Se vi aspettate un servizio di alto livello questo non è l'hotel che fa per voi.",                                        # 1
            "La manutenzione nelle stanze e negli spazi comuni lascia molto a desiderare.",                                            # 1
            "L'organizzazione dei servizi nelle stanze/camere è carente e male gestita.",                                              # 1
            "L'acqua calda in realtà è solo/appena tiepida.",                                                                          # 2
            "Mancavano cose basilari come l'acqua calda e il phon.",                                                                   # 1
            "E' mai possibile che un albergo a 5 stelle non metta/dia qualche bottiglia d'acqua omaggio nel frigobar?",                # 2 = 141 -> 273
            "Il bagno della camera assegnata dalla reception era sporco e non funzionante, ma nessuno ha risposto alle nostre lamentele.",
            "Nonostante avessi richiesto camera con bagno privato, la reception ci ha dato una stanza con bagno condiviso. Esperienza molto negativa.",
            "La reception non ha gestito bene il problema del bagno rotto nella nostra camera, causando disagio durante il soggiorno.",
            "La musica ad alto volume proveniente dalla hall disturbava il riposo, ma la reception non ha fatto nulla per risolvere il problema.",
            "Rumori molesti e musica fino a tarda notte vicino alla reception, nessun intervento da parte dello staff nonostante le nostre segnalazioni.",
            "La reception non ha gestito bene il problema della musica troppo alta proveniente dal bar dell’hotel, rendendo il soggiorno molto sgradevole.",
            "Nonostante le lamentele per la musica e il rumore nelle camere, nessuno è intervenuto per migliorare la situazione."
        ]
    },
    'F&B': {
        'pos': [
            "Colazione/breakfast abbondante e di buona qualità.",                                                                        # 2
            "Personale del ristorante gentile e attento/scrupoloso.",                                                                    # 2
            "Cibo fresco/sano e ben presentato/servito.",                                                                                # 4
            "Una bella/stupenda sala ristorante con un menu squisito. Colazione a buffet, salata e dolce con paste fresche.",            # 2               
            "La colazione all'italiana a buffet è stata abbastanza soddisfacente e ricca e consumata in una sala molto accogliente",     # 1
            "Siamo arrivati ben oltre/dopo l'orario della cena ma non ci hanno negato un piatto caldo.",                                 # 2        
            "La cucina è buona, si mangia discretamente ed il servizio in sala da pranzo attento alle richieste e cortese nei modi.",    # 1
            "Il cibo era incredibile e il personale era altrettanto sorprendente/stupefacente.",                                         # 2
            "Sia i calamari che la torta di granchio erano eccellenti/buonissimi.",                                                      # 2
            "Servizio/prestazione eccellente, cibo incredibile. La sala/zona ristorante è molto bella.",                                 # 4
            "Sempre ottimo cibo e perfetti abbinamenti/accostamenti col vino.",                                                          # 2
            "Complimenti/Congratulazioni anche allo staff in cucina, tutto molto buono.",                                                # 2
            "L'albergo offre la possibilità di mangiare/pranzare tra le vigne ed è una bellissima esperienza.",                          # 2
            "Luogo/Posto e atmosfera incantevole, cibo buonissimo.",                                                                     # 2
            "Qualità del cibo superba, personale di sala e cucina attento/meticoloso e molto cordiale.",                                 # 2
            "Cibo squisito, piatti ricercati/raffinati e studiati, sia nei sapori che nelle presentazioni.",                             # 2
            "I vini serviti durante i pasti sono il fiore all’occhiello, tutti di propria produzione e davvero gustosi.",                # 1
            "Ottima materia prima e ben presentata/servita in piatti creativi.",                                                         # 2
            "Servizio impeccabile e tutti molto educati, qualità altissima del cibo.",                                                   # 1
            "Piatti autentici preparati con maestria e cura, una spanna al di sopra della media dei ristoranti della zona/località.",    # 2
            "Porzioni sempre/molto abbondanti e ottima qualità del cibo.",                                                               # 2
            "Cena squisita, risotto limone e scampi eccellente. Si percepisce l'altissima qualità degli ingredienti.",                   # 1
            "Qualità delle materie prime eccellente, portate ottime e servizio cordiale e impeccabile",                                  # 1
            "I piatti proposti sono semplici ma preparati con grande maestria/bravura, qui ritrovi i profumi e i sapori di una volta",   # 2
            "La colazione a buffet era ricca e ben organizzata, con tante opzioni fresche e il personale sempre disponibile.",           # 1
            "Il servizio in camera è stato rapido e preciso, con piatti caldi e ben presentati consegnati direttamente in camera.",      # 1
            "Il personale di sala è stato sempre cortese e attento, pronto a consigliare piatti e vini con grande professionalità.",     # 1
            "Abbiamo apprezzato molto la gentilezza e la disponibilità del cameriere, che ha reso la nostra cena davvero piacevole.",    # 1 -> 50
            "Apprezzo/gradisco/approvo molto l’uso di ingredienti biologici e a km zero, si sente la differenza nel sapore/gusto.",      # 6
            "Il menù propone/suggerisce piatti originali e creativi, un’esperienza culinaria/gastronomica unica/indimenticabile.",       # 8
            "Ogni portata/pietanza è un’esplosione di sapori e profumi, presentata/esibita con grande cura.",                            # 4
            "Il piatto corrisponde esattamente alla descrizione del menù, nessuna sorpresa.",                                            # 1
            "Personale attento/pronto e disponibile a modificare/variare i piatti per le mie allergie.",                                 # 4
            "La degustazione di vini abbinati ai piatti è stata perfetta, consigliata!",                                                 # 1
            "Il servizio in camera è stato puntuale/tempestivo e preciso/rigoroso, molto comodo.",                                       # 4
            "Ottimo rapporto qualità-prezzo, piatti di qualità a prezzi giusti/corretti.",                                               # 2 
            "Cenone di capodanno ottimo, gentilezza e professionalità dello chef e del personale di sala impareggiabile/incomparabile.", # 2
            "Colazione in camera ottima e rigenerante con vista panoramica mozzafiato/emozionante.",                                     # 2
            "Abbiamo dormito nel B&b e cenato/pranzato nella struttura, tutto divino/superbo!",                                          # 4
            "Cena al ristorante interno top, con un menù non troppo ampio ma sufficiente per soddisfare ogni esigenza/necessità.",       # 2 
            "Ogni pasto viene preparato al momento in una splendida cucina a vista.",                                                    # 1
            "Il cameriere è stato molto gentile/affabile e sempre disponibile.",                                                         # 2
            "Servizio ottimo, camerieri preparati anche alle domande sui prodotti locali ad esempio il vino.",                           # 1
            "Ottima cucina di pesce fresco, buona scelta di vini, servizio gentile e attento.",                                          # 1
            "Bellissime serate in questo hotel, sia per un aperitivo cenato al tramonto che per una ottima cena.",                       # 1
            "Che dire, veramente il top. Ottimo il cibo e le specialità suggerite/proposte dallo staff.",                                # 2
            "Location suggestiva/affascinante e con ottimi taglieri per aperitivo.",                                                     # 2 -> 100
            "Ottimi i vini di loro produzione e squisiti i piatti da poter abbinare/combinare.",                                         # 2
            "Al ristorante interno vasta/ampia scelta soprattutto sui vini locali/autoctoni.",                                           # 4
            "Cibo buono, scelta ampia e con opzioni/possibilità vegane o vegetariane.",                                                  # 2
            "Nella sala ristorante, l'albergo offre anche spettacoli/esibizioni dal vivo, bella atmosfera.",                             # 2
            "Personale gentilissimo e cortese. Sangria top. Cestini con triangoli al mais strepitosi.",                                  # 1
            "Bar interno con ottimi cocktail ed ottima musica.",                                                                         # 1
            "Nightclub interno con bellissime sale, ottima musica e ottimo servizio.",                                                   # 1
            "Cibo buono e sfizioso/appetitoso. Prezzi contenuti/bassi. Esperienza fantastica.",                                          # 4
            "L'albergo offre la possibilità di pranzare fronte mare con tavoli e divani per godersi un meraviglioso tramonto.",          # 1
            "Menù con ottima/enorme scelta sia di piatti/cibo che di vino/bevande.",                                                     # 8
            "Musica in sottofondo, con cocktail e stuzzichini deliziosi.",                                                               # 1
            "La struttura offre molti tavoli e gazebo a pochi metri/passi dal mare/lago.",                                               # 4
            "Il menù è più che valido, con tanti prodotti e ricette tipiche/caratteristiche del luogo/territorio.",                      # 4
            "Il costo è medio-alto ma vale assolutamente/sicuramente la pena andarci e anche ritornarci!",                               # 2
            "Apericena sulla terrazza/loggia al tramonto, un’esperienza indimenticabile. Location unica e suggestiva.",                  # 2
            "Un'esperienza imperdibile/irrinunciabile, prodotti del territorio, musica in sottofondo e spettacoli dal vivo.",            # 2
            "Cenare/Mangiare in quest'hotel è stata un'esplosione di sapori/gusti.",                                                     # 4
            "Ambiente ideale per stare con gli amici e gustare un buon cocktail guardando/ammirando il tramonto.",                       # 2
            "Una nota di merito al personale di sala e di cucina per l’accoglienza e l’attenzione dedicata ai clienti.",                 # 1
            "La sala ricevimenti è un luogo meraviglioso, sia per il cibo, gli arredi, il personale e la musica.",                       # 1
            "Qualità del cibo ottima, con ingredienti a km 0. Pane sfornato da loro, olio biologico e verdure del loro orto.",           # 1 -> 150
            "Personale eccellente e ottime bevande al bar dell'hotel.",                                                                  # 1
            "Apprezzabile/Encomiabile/lodevole l'offerta esclusivamente vegetariana e vegana.",                                          # 3
            "Vini e pietanze senza paragone/confronto. Location top. Consigliato/Suggerito.",                                            # 4
            "Cibo sfizioso tipico/caratteristico del posto. Personale gentile e cordiale.",                                              # 2
            "Buono l’aperitivo offerto all'arrivo e la scelta presente nella carta dei vini, prezzi nella media.",                       # 1
            "Il personale è gentile e disponibile. Menù vegetariano/vegano di ottima qualità.",                                          # 2
            "I prezzi delle portate sono adeguati alla qualità e al servizio che viene offerto, cioè gentile e professionale.",          # 1
            "Abbiamo fatto un aperitivo e cenato con dell'ottimo vino proposto dal ragazzo che ci ha servito.",                          # 1
            "Si possono scegliere i piatti da accompagnare al vino o al cocktail anche al bar. Cibo vegetariano cucinato molto bene.",   # 1
            "Buonissime le birre di loro produzione e molto buono anche il cibo servito.",                                               # 1
            "Al bar interno è possibile sorseggiare ottimi vini in ottima compagnia.",                                                   # 1
            "Esperienza ottima! Piatti appetitosi e ricercati.",                                                                         # 1
            "Cibo di alta/elevata qualità, molto curata anche la presentazione. Prezzi sotto/inferiori la media.",                       # 4
            "I piatti sono molto ben curati/selezionati, il cibo è buono, il personale simpatico/accogliente.",                          # 4
            "Nelle sale interne ascolti musicali e degustazioni enologiche.",                                                            # 1
            "Abbiamo prenotato per una CENA AL BUIO. È stata un’esperienza indimenticabile/memorabile, emozionante.",                    # 2
            "Una esperienza culinaria meravigliosa all’intento di un contesto/ambiente semplice ma molto curato.",                       # 2
            "Menu e vini di ottima qualità, personale attento e professionale con un ottima predisposizione verso gli ospiti.",          # 1
            "Ottimo cibo di stagione, prezzi giusti, accoglienza al top.",                                                               # 1
            "Il ristorante interno offre un’esperienza gastronomica raffinata e consapevole.",                                           # 1
            "Il menu è un viaggio nella delicatezza, con sapori bilanciati alla perfezione e una leggerezza che non è mai banalità",     # 1
            "Le materie prime sono selezionate con una filosofia chiara: stagionalità, filiera corta e rispetto per chi le produce.",    # 1
            "Ogni piatto è una celebrazione dell’equilibrio, dove la tecnica esalta senza mai sovrastare la purezza degli ingredienti.", # 1
            "Un punto di forza è la carta dei vini, attentamente curata/selezionata con etichette biologiche.",                          # 2
            "Il servizio F&B interno è impeccabile: attento ma mai invadente; staff preparato e appassionato/entusiasta.",               # 2
            "Una cucina etica, delicata e straordinaria, che lascia nel cuore la stessa leggerezza che si sente nel palato.",            # 1
            "Personale gentile , vino di loro produzione, ottimi drink/aperitivi.",                                                      # 2
            "Siamo stati a cena e ci siamo trovati benissimo. Piatti molto interessanti e atmosfera accogliente",                        # 1
            "Il b&b serve anche ottimo cibo in un ambiente che sa di famiglia, assolutamente/decisamente da provare.",                   # 2
            "Buon cibo, vino prodotto dalla loro cooperativa. Un processo di inclusione che rende questo posto accogliente e positivo.", # 1
            "Sono celiaco/allergico quindi apprezzo la vasta scelta sul menu. Il servizio era eccellente e l'atmosfera felice.",         # 2
            "Prezzi adeguati/corretti e qualità del cibo elevata/superiore.",                                                            # 4
            "Cibo molto buono, rapporto qualità-prezzo adeguato/giusto e soprattutto personale cordiale.",                               # 2
            "Materia prima eccellente ed esaltata/valorizzata sapientemente dalla cottura impeccabile.",                                 # 2
            "Molta varietà di bruschette e focacce, farcite con prodotti stagionali. Dolci artigianali e veramente buoni.",              # 1 -> 210         
            "Sapori autentici, ricette curate nei minimi dettagli/particolari, presentazioni bellissime da vedere oltre che da gustare.",# 2
            "Un punto di riferimento per chi ama la cucina vegana e per chi desidera scoprire quanto possa essere deliziosa.",           # 1
            "Dehor interno all'albergo molto carino e ben curato/strutturato. Buon servizio e buon cibo.",                               # 2
            "Al bar dell'albergo è possibile sorseggiare/bere ottimi drink preparati da un barman molto preparato.",                     # 1
            "La zona colazione è in una bella sala decorata, piena di atmosfera/colori.",                                                # 2
            "Colazione e cena a buffet buoni. Personale cordiale e accomodante",                                                         # 1
            "La colazione era buona con una scelta varia e un drink rilassante al bar la sera ottimo.",                                  # 1
            "I magnifici murales del ristorante e gli splendidi interni decorati erano deliziosi.",                                      # 1
            "Abbiamo avuto un prosecco in omaggio/regalo nella nostra camera che è stato un gesto molto bello/apprezzato.",              # 4
            "Buffet aperto molto ricco e soddisfacente. E' possibile anche ordinare alla carta per la colazione.",                       # 1
            "La colazione è ottima, ma alcune opzioni in più per i vegetariani sarebbe una bella aggiunta.",                             # 1
            "La mini lounge esterna è perfetta per un caffè/cappuccino mattutino.",                                                      # 2
            "Il bar interno offre qualsiasi tipo di colazione/breakfast, continentale e non.",                                           # 2
            "Abbiamo fatto un pasto di 3 portate al ristorante, delizioso. La colazione giornaliera era più che adeguata.",              # 1
            "Nell'albergo è presente una terrazza panoramica dove è possibile sorseggiare ottimi drink.",                                # 1
            "L'hotel dispone di un bar e un ristorante di dimensioni adeguate e ben funzionante.",                                       # 1
            "Bar e lounge molto belli/curati e con un servizio ottimo e attento.",                                                       # 2
            "Abbiamo particolarmente apprezzato l'abbondante colazione a buffet che offriva opzioni sia calde che fredde.",              # 1
            "La colazione era molto buona con molta scelta e abbiamo apprezzato molto il pranzo che abbiamo fatto nel ristorante.",      # 1
            "Il ristorante dell'hotel serve cibo/vino delizioso. Da provare assolutamente.",                                             # 2
            "Colazione giornaliera inclusa/compresa nella tariffa ottima! Selezione di cibo fresco e assortimento di prodotti delizioso.",#2
            "Colazione a buffet in stile americano davvero/veramente spettacolare/deliziosa con molte opzioni/scelte.",                  # 8 -> 250
            "Quando siamo partiti ci hanno fornito/regalato una colazione da asporto spettacolare/sorprendente!",                        # 4
            "Abbondante e ottima colazione in camera tutte le mattine. Ottimo",                                                          # 1
            "L'albergo offre/dà la bellissima possibilità/opportunità di pranzare sul proprio balcone privato.",                         # 4
            "La colazione a buffet è stata uno dei momenti migliori del nostro viaggio/soggiorno.",                                      # 2
            "Lo chef dell'hotel ci ha dato ottimi consigli sui piatti da ordinare.",                                                     # 1
            "In albergo è presente uno chef molto creativo che prepara ottimi piatti.",                                                  # 1
            "Chef, cuochi, camerieri e tutto il personale di ristorazione davvero bravi.",                                               # 1
            "Albergo sopra la media per servizi di f&b interni, sia al bar che al ristorante.",                                          # 1 = 132 -> 265
            "Il cameriere è stato molto gentile e attento, rendendo la nostra cena davvero piacevole e rilassante.",
            "Ottima qualità dei piatti e servizio impeccabile da parte del cameriere, torneremo sicuramente."
        ],
        'neg': [
            "Prima colazione scarsa/insufficiente e poco varia.",                                                                        # 2
            "Servizio lento/pigro ai tavoli e personale/cameriere poco cortese.",                                                        # 4
            "Cibo di bassa/scarsa qualità e poco/non appetitoso/saporito.",                                                              # 8
            "Cucina/pietanze da ospedale/clinica, più che ristorante.",                                                                  # 4
            "Il cibo era terribile/pessimo/penoso. Carne sempre dura o poco cotta.",                                                     # 3
            "Tutti i piatti sono troppo salati/conditi. Lunga coda/attesa per il cibo appena cotto/preparato.",                          # 8
            "Ho trovato un capello/pelo nel mio cibo/piatto, due volte.",                                                                # 4
            "L'unico succo di frutta che hanno è d'arancia, se non ti piace non bevi nulla. Brioche pessime/scadenti/gommose.",          # 3
            "La colazione potrebbe avere più opzioni di croissant e caffè specialmente per le persone con diete diverse.",               # 1
            "Nessuna/niente colazione in questo hotel; abbiamo dovuto cercare il bar più vicino!",                                       # 2
            "La colazione è costituita da un buono per il bar nella via parallela e consiste in un cappuccino e un cornetto. Misera.",   # 1
            "Colazione praticamente inesistente/irrilevante e quel poco che c'era, di scarsissima/bassissima qualità.",                  # 4
            "Per colazione non c'è alcuna/molta scelta, oltre un cappuccino o caffè, nient'altro.",                                      # 2
            "Colazione un po' misera nelle quantità/volume e qualità dozzinale/mediocre.",                                               # 4 -> 50
            "Colazione povera: servizio lento, brusco e generalmente sub standard.",                                                     # 1
            "Per colazione uno ZERO assoluto/totale.",                                                                                   # 2
            "La colazione è a dir poco povera, con cornetti freddi e gommosi/vecchi.",                                                   # 2
            "Penso/credo che alla caritas vengano serviti prodotti di qualità migliore/superiore.",                                      # 4
            "La stanzetta per la colazione è piccola/minuscola e bisogna aspettare/attendere che si liberano i tavolini/posti.",         # 8
            "Quando siamo andati a fare colazione, le brioche erano già finite/esaurite.",                                               # 2
            "La colazione era disponibile alle due macchinette automatiche presenti nella cosidetta hall.",                              # 1
            "La colazione inizia alle 9.30 quindi se devi uscire prima, anche se l'hai pagata, niente/nulla.",                           # 2
            "Cibo scarso/insufficiente, pietanze/vivande non appetibili/allettanti e poca varietà di genere.",                           # 8
            "Il cibo definito gourmet, era invece scadente e cucinato male.",                                                            # 1
            "I camerieri cominciano a sparecchiare/sgombrare il nostro tavolo nonostante stessimo ancora finendo il primo piatto.",      # 2
            "Bar poco fornito/attrezzato e caffè bruciato. Colazione medio bassa.",                                                      # 2
            "Quello che offre il menù è davvero troppo poco.",                                                                           # 1
            "Il servizio lascia a desiderare, mancavano quasi sempre i piatti al momento dell'arrivo della portata.",                    # 1
            "Abbiamo atteso invano il somelier per dei consigli/suggerimenti sul vino, che non è mai arrivato.",                         # 2
            "Alla richiesta/domanda se il pesce fosse crudo o cotto ci è stato risposto Boh!",                                           # 2
            "Abbiamo ordinato primi di pesce: spaghetti alle cozze e spaghetti con pescatrice, entrambi cucinati in modo pessimo.",      # 1
            "Il vino che dovrebbe essere il punto di forza è accettabile/passabile ma niente di straordinario.",                         # 2
            "Ci hanno servito dei vini veramente discutibili.",                                                                          # 1
            "L'agnello è stato cotto sulla stessa griglia del pesce.",                                                                   # 1
            "Ti promettono contorni di verdure dell'orto ma tutto quello che ti arriva è una patata al forno con salsa barbecue.",       # 1
            "Pesce non fresco. Lo scampo era certamente avariato ma, ahimè lo abbiamo scoperto solo un’ora dopo.",                       # 1
            "Qualità delle materie prime e competenza della cucina oltremodo sotto la media/sufficienza.",                               # 2 -> 100
            "Scelta limitata/ristretta di piatti, mancanza di opzioni per diete particolari/specifiche (vegetariani, vegani).",          # 4
            "Piatti poco curati nell’aspetto, porzioni troppo piccole/scarne.",                                                          # 2
            "Servizio lento e disorganizzato nel servire cibo e bevande. Attese interminabili e piatti giunti freddi.",                  # 1
            "I tavoli erano sporchi/lerci/luridi e le stoviglie non pulite/sanificate correttamente.",                                   # 6
            "Rumore/frastuono eccessivo al ristorante, temperatura sgradevole, arredamento poco confortevole e trascurato.",             # 2
            "Durante ogni servizio c'è sempre la telecronaca di qualche partita ad altissimo volume.",                                   # 1
            "Prezzo decisamente troppo alto/elevato rispetto alla qualità espressa.",                                                    # 2
            "Hanno sbagliato piatti e sbagliato le ordinazioni/comande 2 volte durante la stessa cena.",                                 # 2
            "Hanno sostituito/modificato degli ingredienti esauriti/terminati con altri diversi senza avvisarci.",                       # 4
            "L’evento a tema organizzato dal ristorante è stato deludente: pochi piatti, male assortiti e personale impreparato.",       # 1
            "Ho ordinato pranzo/cena in camera e dopo un’ora ancora non avevo ricevuto nulla, senza alcuna spiegazione dal personale.",  # 2
            "Il cameriere era scortese e sembrava infastidito/seccato dalle nostre domande sul menù.",                                   # 2
            "Nonostante le nostre richieste, il personale di sala è stato poco attento e ha dimenticato alcune portate.",                # 1
            "Promettono/Assicurano prodotti locali ma spesso servono cibi industriali e poco freschi.",                                  # 2
            "Piatti troppo elaborati/complessi che non rispettano/rispecchiano i sapori tradizionali, deludente.",                       # 4
            "Cibo insipido/scialbo e presentazione trascurata, non invoglia a mangiare.",                                                # 2
            "Il menù promette piatti ricchi ma arriva sempre qualcosa di molto diverso.",                                                # 1
            "Non hanno saputo gestire la mia intolleranza, rischio allergia evitabile.",                                                 # 1
            "L’evento di degustazione è stato mal organizzato/gestito, vini non abbinati bene/correttamente.",                           # 4
            "Il ristorante chiude troppo presto, impossibile cenare tardi.",                                                             # 1
            "Prezzi troppo alti/elevati per la qualità offerta, non vale la pena.",                                                      # 2
            "Tempi biblici/lunghissimi tra una portata e l'altra e un pezzo di plastica nella macedonia.",                               # 2
            "Peccato che per i celiaci non abbiano nulla da mangiare/servire se non 2 arachidi e 4 semi di zucca.",                      # 2 -> 150
            "Personale/addetti ma soprattutto titolari/proprietari molto sgarbati e classisti.",                                         # 4
            "Aperitivo annacquato che non sapeva di nulla.",                                                                             # 1
            "Menù troppo limitato/ristretto e poche/scarse alternative per bambini.",                                                    # 4
            "Un po’ di confusione/caos nella gestione delle prenotazioni e delle varie formule proposte.",                               # 2
            "Non ci sono state date indicazioni/informazioni chiare sul cibo e questo ha penalizzato l'esperienza.",                     # 2
            "Abbiamo ordinato due calici di sangria accompagnati da un tagliere misto. La qualità del cibo è stata piuttosto scarsa.",   # 1
            "Cocktail e pasti preparati in modo sbrigativo e senza troppa fantasia.",                                                    # 1
            "Nel ristorante interno, la playlist proposta risultava poco in linea con l’ambiente e l’atmosfera.",                        # 1
            "Troppo caos. Bambini fuori controllo che correvano ed urlavano ovunque.",                                                   # 1
            "Molti aspetti migliorabili sul piano dell’organizzazione e del servizio ai tavoli.",                                        # 1
            "Nessuna possibilità di pranzare/cenare in camera. Inaccettabile in un 5/4 stelle.",                                         # 4
            "Aperitivo da migliorare, non all'altezza del posto. Prezzi leggermente alti.",                                              # 1
            "Sono arrivati a prenderci l'ordine dopo circa mezz'ora dall'ingresso/arrivo.",                                              # 2
            "Cibo pessimo, chiacchere/conversazioni a voce alta e scortesia.",                                                           # 2
            "Il barman ha rotto un bicchiere mentre preparava il mio cocktail.",                                                         # 1
            "Scortesi, poco chiari/trasparenti, cibo surgelato.",                                                                        # 2
            "Gli arrosticini sono tutto grasso e la carne è stopposa, esperienza pessima/deludente,",                                    # 2
            "Pessimo rapporto qualità prezzo.... Molti piatti sono stati rimandati indietro.",                                           # 1
            "Purtroppo siamo stati/rimasti fortemente delusi dai piatti che ci hanno servito.",                                          # 2
            "Abbiamo trovato poca elaborazione e ricerca, sopratutto/specialmente nei secondi piatti.",                                  # 2
            "Le porzioni erano davvero scarse rispetto al prezzo. La mia bistecca si è rivelata una fettina quasi impercettibile.",      # 1
            "Cucina vegetariana sminuita/sottovalutata e banalizzata; poca scelta e mediocrità nei piatti.",                             # 1
            "Menu degustazione molto deludente e ad un prezzo/costo elevatissimo.",                                                      # 2
            "Il menù del giorno è ciò che è avanzato/rimasto in cucina dal giorno prima.",                                               # 2
            "Fritti unti e cotti male. Se potete evitate di mangiare qui.",                                                              # 2
            "le sedie e tavoli della sala colazione non sono confortevoli. Niente tovaglie e servizio molto sbrigativo.",                # 1
            "Alle 8 di mattina il buffet della colazione è già praticamente vuoto. Abbiamo dovuto fare colazione al bar.",               # 1
            "Nessun bar serale per bevande al rientro in hotel. Desolante.",                                                             # 1
            "La colazione in sé era limitata e di scarsa qualità. Meglio fare colazione altrove.",                                       # 1
            "Non riesco a capire perché servano una tazza di caffè così schifosa in un hotel così costoso.",                             # 1 -> 200
            "Caffè e cappuccini serviti a colazione erano orribili/terribili.",                                                          # 2 
            "Nei pranzi e nelle cene a buffet, pochissimo assortimento.",                                                                # 1
            "I pasti sarebbero dovuti essere genuini e freschi ed invece è tutto cibo in scatola.",                                      # 1
            "Tutte le portate/pietanze avevano qualche difetto/errore. In generale poco gusto e niente raffinatezza/ricercatezza.",      # 8
            "In un albergo non è accettabile/tollerabile che per colazione non servano tè.",                                             # 2
            "Ogni volta che cucinano nell'abergo, un tanfo di cipolla fritta si spande/estende per tutte le camere.",                    # 2
            "Colazione appena passabile con poca offerta/varietà di salato e vegano.",                                                   # 2
            "Evitate la colazione in hotel; in zona si trovano opzioni/situazioni decisamente migliori.",                                # 2
            "Colazione a 15 euro a persona in albergo! Mi aspetto di mangiare/gustare una bistecca. Da evitare.",                        # 2
            "La colazione compresa nel prezzo prevede 2 fette biscottate e una vaschetta di marmellata/confettura.",                     # 2
            "Tutti i prodotti assaggiati sono industriali e veramente di scarsa qualità, non in linea con il resto.",                    # 1
            "L'albergo è pubblicizzato/reclamizzato come dotato di un bar-ristorante, cosa che forse è così, ma non è aperto.",          # 2
            "La colazione servita con estrema scortesia/antipatia; sembra non vedano l'ora che tu te ne vada.",                          # 2
            "Dolci stantii e biscotti secchi. Una colazione da terzo mondo.",                                                            # 1
            "Il ristorante interno è perentemente pieno. Non c'è stato verso di pranzarci una volta.",                                   # 1
            "Abbiamo provato a chiedere la colazione in camera e ci hanno riso in faccia.",                                              # 1
            "Credo che il cameriere abbia sputato nel mio cappuccino. Non l'ho bevuto.",                                                 # 1
            "Il personale non mi dava l'idea di igiene e pulizia, ragion per cui non ho mai pranzato in albergo.",                       # 1
            "Tutta la struttura è fatiscente/decadente, in particolare la zona della colazione, pranzo e cena. Cibo così così.",         # 2
            "Da un 5 stelle mi aspetto una qualità del cibo eccelsa e invece era appena passabile.",                                     # 1
            "La colazione viene servita in uno scantinato. Sembra di essere in una cantina puzzolente e ammuffita.",                     # 1
            "I pasti in hotel non sono per niente soddisfacenti. Meglio cercare un locale all'esterno.",                                 # 1
            "Ci sono tantissimi posti/locali nei paragi/pressi dell'hotel in cui si mangia molto meglio.",                               # 4
            "Per tutta la durata della vacanza, il ristorante interno era chiuso per lavori e non abbiamo mai potuto pranzarvi.",        # 1
            "Offrire una colazione solo salata in Italia non è accettabile. Pur avendola pagata non ne ho usufruito.",                   # 1
            "Non hanno potuto, saputo o voluto soddisfare le mie esigenze/abitudini alimentari.",                                        # 2
            "Il personale del bar al piano superiore era sempre molto poco cordiale.",                                                   # 1
            "I pasti/cibi/dessert in quest'albergo sono all'insegna del risparmio.",                                                     # 3 -> 251
            "Servizio/prestazione di colazione deludente. C'è bisogno di molte più attenzioni/cure per i clienti.",                      # 4  
            "Materie prime economiche e cucina perennemente in ritardo sulle ordinazioni/richieste.",                                    # 2
            "Buffet troppo piccolo e perennemente affollato/accalcato. Scene fantozziane/comiche.",                                      # 4
            "Ho esigenze alimentari specifiche ma non c'è stato verso di farle rispettare al personale di ristorazione.",                # 1
            "Sto seguendo una dieta/alimentazione particolare ma cuoco e camerieri se ne sono infischiati/disinteressati.",              # 4 = 122 -> 266
            "La cena al ristorante è stata un’esperienza negativa: il cameriere ha sbagliato l’ordine e non si è scusato.",
            "I piatti serviti al ristorante erano deliziosi, ma il servizio del cameriere è stato lento e poco professionale.",
        ]
    }
}

# Funzione per generare tutte le recensioni possibili da tutte le frasi base e varianti
def genera_tutte_recensioni():
    recensioni_set = set()    # Crea un insieme/collezione non ordinata di elementi unici
    recensioni = []
    id_corrente = 1
    for reparto in frasi_base:
        for sentiment in frasi_base[reparto]:
            for frase_base in frasi_base[reparto][sentiment]:
                varianti = genera_varianti(frase_base)
                for frase in varianti:
                    titolo = ' '.join(frase.split()[:3]) + '...'   # Creiamo un titolo prendendo le prime 3 parole
                    chiave = (frase, reparto, sentiment)           # Creiamo una tupla come chiave per evitare duplicati
                    if chiave not in recensioni_set:               # In questa versione dello script non dovrebbero comparire frasi duplicate,
                        recensioni_set.add(chiave)                 # ma in alcuni casi, frasi base diverse potrebbero dar luogo a frasi
                        recensioni.append({                        # duplicate una volta sviluppate tutte le combinazioni. Usare una tupla
                            'id': id_corrente,                     # come chiave è un modo semplice e veloce per identificare univocamente  
                            'title': titolo,                       # ogni recensione in base al testo, reparto e sentiment.
                            'body': frase,                  
                            'department': reparto,                 # Popoliamo l'array (lista) recensioni con tutti i campi
                            'sentiment': sentiment
                        })
                        id_corrente += 1
    return recensioni

# Funzione per salvare il dataset in CSV con separatore pipe

def salva_csv(recensioni, filename):
    campi = ['id', 'title', 'body', 'department', 'sentiment']
    with open(filename, 'w', newline='', encoding='utf-8') as f:     # "with" garantisce che le risorse vengano aperte e chiuse al termine
        writer = csv.DictWriter(f, fieldnames=campi, delimiter='|')  # scrive nel file "f"
        writer.writeheader()
        for r in recensioni:
            writer.writerow(r)

if __name__ == '__main__':    # Eliminabile in questo caso ma buona prassi tenerlo.
                              # condizione speciale in Python che serve a distinguere quando uno script viene eseguito direttamente (ad esempio da terminale o
                              # o IDE) oppure quando viene importato come modulo in un altro script. In pratica: Se esegui direttamente lo script 
                              # generadataset.py, il valore di __name__ sarà proprio la stringa '__main__', quindi il blocco di codice dentro 
                              # if __name__ == '__main__': verrà eseguito.
                              # Se invece importi generadataset.py da un altro script (ad esempio con import generadataset), il valore di __name__ 
                              # sarà il nome del modulo ('generadataset') e quindi quel blocco non verrà eseguito automaticamente.
                              # Questo meccanismo serve a: consentire che alcune parti di codice (come test, esecuzioni di script, generazione di file, demo)
                              # vengano eseguite solo quando lo script è lanciato direttamente. 
                              # Evitare che queste parti si eseguano in modo indesiderato quando lo script è importato come libreria o modulo.

    dataset = genera_tutte_recensioni()  # Genera tutte le recensioni uniche possibili
    print(f"Generato un totale di {len(dataset)} recensioni uniche.")
    percorso_file = 'C:/Users/idset/Desktop/UniPegaso/Project work/datasetliv1.csv'  # Quando usi funzioni come pandas.DataFrame.to_csv(percorso_file), 
    salva_csv(dataset, percorso_file)                                                # il file CSV viene scritto esattamente in quel percorso con quel nome.
    print(f"Generato file datasetliv1.csv con {len(dataset)} recensioni.")


    