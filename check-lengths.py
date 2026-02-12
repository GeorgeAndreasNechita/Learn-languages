import deepl
import pandas as pd
import re
import json

def translate_and_save(text):
    # 1. Text teilen (nach Punkt, Komma, Semikolon)
    gefilterter_text = re.sub(r'([.,;?:])\s*', r'\1\n', text)
    zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]
    print(gefilterter_text)



MEIN_TEXT = """ Di quest’etá in generale?, ed in particolare: di questo periodo primo
delle preponderanze spagnuola e francese combattute [1492-1559].—Fin
dall’ultimo secolo dell’etá precedente, noi vedemmo incominciare quel
travaglio di unione dei popoli, d’ingrandimento degli Stati italiani, il quale
continuò lungo tutta l’ultima e durante nostra etá. E noi, salutammo
siffatte riunioni con compiacimento, senza guari compiangere le forme
repubblicane perdutesi in quell’opera, senza lamentare i principati sorti
sulle loro rovine; perché crediamo, che anche ne’ principati possa esser
libertá e felicitá; perché ai tirannici e semibarbari di que’ secoli ne
succedettero di quelli civili, e che van diventando liberi; perché poi, in
somma, noi teniam l’occhio fermo principalmente al bene di tutte insieme
le terre italiane, e che, tenendo sempre piú impossibile la riunione totale
di esse, noi stimiamo sommo bene lo sminuzzamento quanto minore, le
riunioni quanto maggiori sieno possibili. Se si fosse continuata quest’opera
delle unioni degli Stati senza invasioni, senza preponderanze straniere,
Dio sa qual magnifico destino sarebbesi venuto ordinando fin d’allora
all’Italia! Dio non volle, pur troppo; i nostri maggiori non se l’erano
meritato; non avean adempiuto ai grandi doveri, alle grandi virtú
nazionali; non avean badato se non ciascuno a sé, con quell’egoismo
politico che è vizio e stoltezza insieme, e tanto piú quanto piú va
progredendo la civiltá. Quindi, quest’etá, che fu felicemente della
formazione degli Stati italiani, fu pure infelicissimamente delle invasioni e
delle preponderanze straniere; e prima, delle due francese e spagnuola
combattenti tra sé per sessantasette anni; poi della spagnuola pesante sola

per centoquaranta; poi delle due, francese ed austriaca, contrappesanti in
guerra o in pace, per centoquattordici altri. E da queste tre combinazioni
diverse di preponderanze verranno poi naturalmente le tre suddivisioni di
quest’ultima etá nostra. Nella quale non faccia specie se dimoreremo piú a
lungo che nell’altre piú lontane. Cosí abbiam fatto, a disegno, fin da
principio. Nelle storie scritte ad uso degli eruditi, si soglion cercare i
particolari de’ tempi quanto piú antichi. Ma nelle storie scritte ad uso
comune, popolare, giovano all’incontro tanto piú i particolari, quanto piú
son di tempi vicini, simili a’ nostri, piú utili ad accennare ciò che sia da
imitare, ciò che da fuggire.—E rimanendo ora nel primo de’ tre periodi
detti, ci par da notare che niuno forse mai quanto quello s’assomigliò ai
tempi nostri. Una delle volgarita di questi è di credere, che non somiglino
a nessun altri, che non mai si sien veduti tanti e cosí grandi fatti, tante e
cosí grandi novitá. Quindi poi due gravi errori, due politiche
contrariamente esagerate e mediocri: di alcuni timidi, spaventati per sé,
od anche candidamente per altrui, di quel moto che par loro anomalo,
pericoloso, e a cui si fanno un dovere di resistere, senza eccezione né
discernimento; di altri avventati e buonamente compiacentisi in ogni
moto, in ogni novitá, e che si fanno un dovere di secondarle, di spingerle,
senza discernimento pur essi. Non molti sanno vedere il proprio tempo
qual è; non molti, che il nostro, pieno di fatti nuovi e progressivi senza
dubbio, è perciò appunto simile ad altri tempi non meno pieni di tali fatti;
diversi l’uno e gli altri in ciò solo, che i progressi posteriori son di lor
natura pur ulteriori; ma di nuovo simili in ciò, che tra le novitá sempre le
une son progressi, e le altre all’incontro arresti o regressi; e che quindi
sempre ogni politica assennata debb’essere discernente, e constare delle
due opere del secondare e del resistere. Ad ogni modo, se niun tempo mai
fu pieno di grandi novitá, certo fu quello che siamo per correr qui dal
1492 al 1559, dalla chiamata di Carlo VIII che turbò l’Italia e la
cristianitá, alla pace di Cateau-Cambrésis che bene o male le compose.—
Trovata la bussola da due secoli, la polvere da guerra da uno e mezzo, la
stampa da un mezzo, le lettere antiche lungo tutto quel tempo, l’astrolabio
da alcuni anni, l’America nell’anno stesso onde incominciamo, la via
dell’Indie per il capo di Buona Speranza due anni dopo [1494];
s’accumularono, si combinarono gli effetti di tutte queste nuove cause; ne
uscí un mondo rinnovato tutto; si rinnovarono, si mescolarono tutte le
nazioni; e n’uscí la cristianitá pur troppo non piú unita in una fede e una
Chiesa intorno a una sedia centrale, ma una cristianitá felicemente unita,
non piú intorno alla barbara monarchia universale di Carlomagno e de’
pseudo-imperatori romani, bensí in una civiltá e una coltura universali. E

il mezzo adoperato a ciò dalla Provvidenza qual fu egli? Evidentemente
quel ritrovo che ella diede a tutte quelle nazioni semibarbare nella nostra
Italia, posseditrice da quattro secoli non solamente del primato, ma della
privativa della libertá e della coltura. Le nazioni non presero, per vero
dire, la libertá italiana, che non era bella, non buona, non civile, non
allettante, e del resto giá semispenta; ma presero quella coltura, di che
abusaron prima religiosamente, di che usaron poi politicamente a
riacquistare la libertá.—E l’Italia intanto? L’Italia che aveva tutti i
vantaggi della libertá, della coltura, dei commerci e delle ricchezze, ma
che aveva i tre grandi svantaggi della libertá mal ordinata, del disuso
nella milizia, e di una indipendenza mal compiuta; l’Italia perdette tutti
que’ vantaggi suoi, tutte quelle sue operositá, e quel poco d’indipendenza;
visse od anzi sopravvisse alcun tempo splendidamente in quegli uomini
sorti al tempo migliore, per cader poi, quanto a politica, a un tratto;
quanto al resto, a poco a poco, in un’abbiezione che, questa sí, fu
anormale, forse unica nella serie de’ secoli civili cristiani.—Furono
dunque questi sessantasette anni uno splendidissimo, spensieratissimo
precipitare e non piú. E quindi peggio che mai resta tormentato qui lo
scrittore di non aver luogo a spiegarli, a lasciarne una chiara ed adeguata
impressione. Ma suppliranno i leggitori, con quel che sa ognuno di questo
nostro tempo di splendore. E suppliran pure a quelle applicazioni a’ propri
tempi, le quali, che dicasi, sono insomma il vero pro della storia; sapran
vedere tutta la serie delle cause, degli effetti, e delle nuove cause di nostre
perdizioni; l’incompiutezza antica dell’indipendenza, l’antico disordine
delle libertá, l’antico difetto d’armi nazionali, gli stranieri nuovamente
chiamati, sofferti, lasciati antiquarsi; e finalmente le operositá nazionali
cessate, gli ozi, i vizi, le mediocritá innaturali all’Italia, accettate quasi
necessitá, diventate abito, e seconda natura; e, danno e vergogna ultima a’
degeneri, il riposar in quel limo, e consolarvisi col sognar le glorie de’
maggiori.
2. Stato d’Europa e d’Italia [1492-1494].—La Provvidenza ha tutto nelle
mani, senza dubbio; ma lascia apparire alcune, e cela altre delle leggi
delle opere sue; e fra le piú celate è forse quella per cui concede o nega
uomini alle nazioni. Fu uno di que’ decreti male scrutabili di lei, che
mentre i popoli oltremontani ed oltremarini si univano dopo lunghi
travagli ciascuno in un corpo di nazione sotto principi se non grandi
almeno arditi ed operosissimi, l’Italia, perduto Lorenzo il magnifico, non
avesse piú se non uomini o mediocri (come giá quelli che eran succeduti a

Cosimo e Francesco Sforza), o cattivi o cattivissimi.—In Inghilterra Arrigo
VII, regnante dal 1485, aveva con suo maritaggio riunite le due case,
distrutte le due fazioni di Lancastro e di York, che l’avevano lungamente
straziata.—In Ispagna s’eran congiunte Castiglia ed Aragona fin dal 1474
con un altro maritaggio tra Isabella e Ferdinando; e questi insieme avean
poi conquistata Granata, l’ultimo regno e rifugio di mori, in quel
medesimo anno [1492] della morte di Lorenzo e della scoperta d’America;
ondeché, non rimaneva piú disgiunto se non il piccol regno di Navarra, e
tutte quelle vittorie e fortune accendevan l’animo piú inquieto che grande,
ma insomma ambiziosissimo di Fernando, detto (appunto allora e per
concessione del papa) il «re cattolico».—In Francia, dove Carlo VII aveva
finita la guerra d’indipendenza e cacciati gl’inglesi, e Luigi XI riunite
Borgogna e Provenza e i diritti de’ secondi Angioini al regno di Napoli e
Sicilia, regnava il giovine Carlo VIII dal 1483; e, riunita Bretagna
sposando Anna che n’era duchessa, ambiva quel retaggio dei conti di
Provenza in Italia, ambiva l’imperio orientale, una gloria da Carlomagno,
qualunque gloria.—Finalmente in Germania, signora nostra (di nome per
vero dire oramai, ma anche i nomi son pericoli ai deboli), succedeva nel
1493 al misero Federigo III d’Austria Massimiliano prodigo, inquieto, ed
egli pure ambizioso. Con tre principi come Ferdinando, Carlo VIII e
Massimiliano a capo di tre quarti della cristianitá, non è meraviglia che
ella si sconquassasse tutta; è piuttosto miracolo che non ne perisse. E
intanto in Italia signoreggiavano, su Savoia e Piemonte, Carlo II, fanciullo
d’un anno, quando succedette nel 1490; su Monferrato, Gian Francesco II
pur fanciullo; su Milano, quasi fanciullo quel giovane ed incapace Gian
Galeazzo, che dicemmo sotto la quasi tutela di suo zio Ludovico il moro, e
che, avendo sposata nel 1489 Isabella di Napoli, n’aveva acquistata in
apparenza una protezione, di fatto un nuovo pericolo, per la gelosia e la
paura concepitene dal Moro. In Firenze erano succeduti alla potenza
indeterminata di Lorenzo, Piero mediocrissimo che non la sapea tenere, e
due fratelli minori, Giovanni, allor cardinale e che fu poi papa Leon X, e
Giuliano. E sulla sedia romana, morto il Cibo nel medesimo anno fatale
1492, era succeduto Borgia, Alessandro VI, il peggior papa di questi
tempi, ove ne furono pochi buoni. Signoreggiavano ne’ ducati di Ferrara e
Modena gli Estensi; in quello d’Urbino, i Montefeltro; i Gonzaga in
Mantova; i Bentivoglio in Bologna; i Baglioni in Perugia; i Colonna, gli
Orsini ed altri signorotti, in molte terre della Chiesa. In Napoli regnava il
perfido e crudele, e cosí diventato potente, ma ora vecchio Ferdinando I,
che non seppe scongiurar il pericolo, che morí prima di succombervi nel
1494. Sicilia era del re cattolico. Genova, tenuta come feudo di Francia da

Ludovico il moro. E Venezia, giá caduta in quella viltá e stoltezza del
volersi tener neutrale ne’ pericoli comuni, isolata. E cessati, con Francesco
Sforza e i Piccinini, i grandi condottieri potenti al par di principi e
repubbliche, non ne rimanevan guari se non de’ piccoli, impotenti a tutto,
salvo che a tener disavvezzi dall’armi i popoli della imbelle Italia.
3. Alessandro VI papa [1492-1503].—La causa de’ nuovi guai d’Italia fu
senza dubbio l’incapacitá politica e militare di lei; l’occasione poi, fu
l’ambizione straniera di Carlo VIII, aiutata dall’ambizione traditrice di
Ludovico il moro. Il quale richiesto da Ferdinando di lasciare il governo al
nepote Gian Galeazzo, volle usurparne il ducato; e perciò fecesene dare da
Massimiliano imperatore l’investitura disprezzata giá dal gran Francesco
Sforza, e non data poi a nessuno dei discendenti. E per poter poi effettuare
l’usurpazione, volle assicurarsi di Carlo giá minacciante, s’alleò con lui, gli
promise passaggio ed aiuto. Qui non era nessuna delle scuse dell’altre
chiamate; non quella, che può esser buona, di cacciare altri stranieri;
nemmen quella cattiva, di resistere a un nemico interno. Qui è un cumulo
di tradimenti; e quindi il Moro è il traditor piá esecrato nelle memorie
italiane. Ma pur troppo non fu il solo; il cardinal Della Rovere, che fu poi
papa Giulio II e fece tanto chiasso di cacciar i barbari d’Italia, spinto ora
dalla rivalitá, dalla inimicizia ad Alessandro VI, anch’egli si trova tra’
chiamatori ed accompagnatori dello straniero.—Carlo scese in agosto
1494 pel Monginevra, Torino, Asti. Ivi ammalò e si fermò. Poi passò a
Milano, visitò, non protesse Gian Galeazzo giá morente, e che morí pochi
di appresso [20 ottobre] con voci di veleno. Cosí il Moro fu duca, e tirò
fuori l’investitura imperiale. Carlo proseguí, s’appressò a Toscana per
Pontremoli. Viene Pier de’ Medici spaventato, e gli dà i castelli fiorentini
che difendean que’ passi, quello stesso di Pisa. Ma tornato costui a
Firenze, è cacciato dalla signoria, dal popolo sdegnato [9 novembre]. Al
medesimo dí, Pisa caccia i fiorentini, si libera, presente, e piú o men
connivente, Carlo VIII. Questi lascia un presidio nel castello, muove a
Firenze, v’entra militarmente, la lancia alla coscia, tratta un accordo colla
nuova signoria; e volendolo imporre duro, gli è stracciato in faccia da Pier
Capponi, che disse:—Sonate vostre trombe, noi sonerem nostre campane.
—Fu il solo bell’atto di questa guerra; cosí vergognosa, del resto, che i
contemporanei la disser fatta col «gesso» dei forieri i quali segnavan gli
alloggi francesi di tappa in tappa. S’accomodarono tuttavia Firenze e
Carlo; e questi proseguí a Roma, dove il papa chiusesi in castel Sant’

Angelo, e s’accomodò poi. Spaventato Alfonso II, il nuovo re di Napoli
testé succeduto, lasciava vilmente la corona a suo figliuolo Ferdinando II
[24 gennaio 1495]; e questi provava a difendere i passi, ma era vilmente
disertato da’ suoi, e fuggiva da Napoli a Sicilia; e Carlo VIII entrava in
quella il dí appresso [22 febbraio]. S’arrendevano, a gara di viltá, castella,
cittá, province, grandi, popoli, il Regno. Tanto che tra pochi dí i francesi
n’erano ad oziare e viziarsi nella disprezzata conquista.—Allora,
sollevavasi tutta Italia, mezza Europa, lo Sforza traditore, perché non avea
piú ad acquistare ma a difendere il ducato, or minacciatogli dalle
pretensioni del duca d’Orléans discendente da una Visconti e signor d’Asti;
Venezia, tornata (per poco) al sentimento de’ pericoli d’Italia; il Borgia,
tornato dal suo spavento; il re cattolico per restaurare i parenti, o forse fin
d’allora riaggiunger Napoli a Sicilia ed Aragona; e Massimiliano non so
per quale delle sue mutevoli ambizioni. Tutti questi insieme firmavano un
trattato contra Carlo [31 marzo]. Il quale cosi minacciato ripartiva da
Napoli [30 maggio]; passava a Roma, schivava Firenze, passava a Pisa; e
varcato Appennino, trovava a Fornovo l’esercito degli alleati italiani
capitanato dal marchese di Mantova. Combattessi addí 6 luglio, molto piú
forti gl’italiani. Disputasi chi vincesse; ma i francesi avean combattuto per
passare, e passarono. Giunsero ad Asti, Carlo vi si fermò a corteggiar
donne e trattar pace col Moro; e fattala, partí [22 ottobre] da Torino per a
Francia, dove non pensò piu guari a Italia.—Tornò quindi Ferdinando II
nel Regno, rientrò in Napoli [7 luglio], e guerreggiandovi poi due anni
contro a’ francesi rimastivi sotto Monpensieri, se ne liberò coll’aiuto degli
spagnuoli capitanati da Gonzalvo di Cordova, il conquistator di Granata,
detto il «Gran capitano». Capitolarono gli ultimi francesi ad Atella, e
moriva Ferdinando II poco dopo, lasciando il regno a Federigo III suo zio,
fratello di Alfonso [1496]. Ed anche da Pisa si erano ritirati i francesi fin
dal primo dí di quell’anno, lasciando disputarsi e guerreggiarsi tra sé
pisani e fiorentini, e per gli uni o gli altri le varie potenze d’Italia, e
Massimiliano re de’ romani. Il quale, invitato anch’egli dal Moro, il gran
chiamator di stranieri, scese a frapporsi in tutto ciò con poca gente e
pochi danari, e quindi non prese le corone solite, non fece nulla, e risalí
disprezzato oltre ogni altro imperatore mostratosi in Italia.—I fiorentini
tentavano intanto riordinar lor repubblica sgombra di Medici; ma eran
divisi in parti, non piú nazionale o straniera, né per il papa o l’imperatore,
per l’aristocrazia o la democrazia, per la repubblica o la signoria, ma pro e
contro un frate domenicano, Gerolamo Savonarola. Costui, zelante,
costumato, austero a sé, aspro ad altrui, in tempi corrotti, avea colle
prediche politiche tratti molti a sé, vivente ancora Lorenzo. Era stato

chiamato al letto di questo morente, e dicesi non l’avesse voluto assolvere,
perché Lorenzo non voleva restituire la repubblica, a modo di lui il frate.
Avea profetato malanni, castighi di Dio, francesi; ed or pendeva a questi
che avean adempiute sue profezie. I suoi partigiani chiamaronsi
«piagnoni»; i contrari, gente di mondo, gentiluomini i pií, «arrabbiati»; i
medii, piú o men desiderosi de’ Medici, «bigi,» e poi «palleschi»; nomi e
parti del paro ignobili. I particolari del tempo son vere commedie; il fine,
tragedia barbarissima, da medio evo che ancor fiorisse. Contrario al frate
riformator di costumi e disciplina ecclesiastica era Alessandro VI,
naturalmente. Gli proibí di predicare. Il frate obbedí per poco; poi
ricominciò, e contro al papa. Allora uscirono da sé, o fecersi uscire contra
lui altri frati; prima un agostiniano, poi un francescano, Francesco di
Puglia, il quale propose una di quelle stoltezze od empietá parecchie volte
condannate dalla Chiesa, un giudicio di Dio: che passassero egli fra
Francesco e il Savonarola tra una catasta ardente; e chi passasse illeso,
quegli vincesse. Savonarola non volle, ma s’offri per lui fra Domenico suo
confratello. Appuntossi il dí 7 aprile 1498; grande aspettativa,
grand’apparecchio, gran concorso. Ma venuti al duello i due frati, fecero
come chi vuole e disvuole, attaccaron disputa sul modo: cioè (quasi
profanazione al dirne), sul Sacramento, che il domenicano volea portar
con sé tra le fiamme, e il francescano non voleva. Non se ne fece altro. Il
popolaccio beffato infuriò, gli «arrabbiati» si sollevarono; e al dí appresso
diedero l’assalto al convento di San Marco, e fecer prigioni fra Gerolamo,
fra Domenico, e un terzo, fra Silvestro. I quali poi furono in pochi dí
interrogati, torturati, condannati, ed arsi in piazza [23 maggio].—Di
Savonarola chi fa un santo, chi un eresiarca precursor di Lutero, chi un
eroe di libertá. Ma son sogni: i veri santi non si servon del tempio a negozi
umani; i veri eretici non muoiono nel seno della Chiesa, come morí,
benché perseguitato, Savonarola; e i veri eroi di libertá sono un po’ piú
sodi, non si perdono in chiasso come lui. Fu un entusiasta di buon conto; e
che sarebbe stato forse di buon pro, se si fosse ecclesiasticamente
contentato di predicare contro alle crescenti corruttele della spensierata
Italia.—Alla quale, come tale, ripullulavano le occasioni di perdizioni. Al
dí appunto della festa fallita in Firenze, era morto Carlo VIII, era salito al
trono di Francia Luigi XII, quel duca di Orléans che giá dicemmo
pretender a Milano come discendente d’una Visconti, e che or pretese a
Napoli come re di Francia, successore ai diritti degli ultimi Angioini. Se gli
fosse riuscito il tutto, incominciava fin d’allora, e a pro di Francia, quella
unione dei due grandi Stati italiani di settentrione e mezzodí, la quale
sessant’anni dopo die’ l’Italia legata in mano a Spagna. Luigi XII non era

avventato come Carlo VIII; era anzi principe prudente, destro, politico, e
in Francia cosí buono che n’ebbe nome di «padre del popolo». Eppure,
anch’egli ebbe le maledizioni d’Italia; tanto i migliori a casa son cattivi
fuori! Non attese dapprima se non a Milano; e que’ veneziani che s’eran
sollevati contro Carlo VIII, si collegaron ora con Luigi XII per il misero
acquisto di Cremona e Ghiara d’Adda [trattato di Blois, 15 aprile 1499].
Chiaro è: que’ vantatissimi politici non ebber forse mai, non aveano certo
piú niuna politica vera, lunga, propriamente detta, ma solamente abilitá
alla giornata; quella vantata aristocrazia non aveva piú l’aristocratica virtú
della costanza, ma solamente l’aristocratico istinto della propria
conservazione. E legossi pure con Luigi XII Alessandro VI, per far suo
infame figliuolo Cesare Borgia duca di Valenza in Francia e di Romagna in
Italia. E lasciaron fare, Massimiliano distratto in Germania, e Federigo III
di Napoli mal fermo nel nuovo regno. Cosí da Asti, giá sua, Luigi XII assalí
il ducato; ed alle prime fazioni sbandaronsi le truppe del Moro, che fuggí
in Germania; e Luigi entrò in Milano [2 ottobre 1499], e tutto il ducato
con Genova furono di lui. Ma tornato esso in Francia, e riposando i
francesi lasciati nella conquista, ritorna il Moro con un esercito di svizzeri
e fuorusciti, e riprende Como, Milano, Parma, Pavia, Novara. Arriva La
Tremoglia con un nuovo esercito di francesi e svizzeri. Svizzeri di qua,
svizzeri di lá, dicesi ricevessero da lor paese ordine di non combattersi. Ad
ogni modo quelli dello Sforza lasciano in mano agli altri e a La Tremoglia
i lor compagni italiani, i Sanseverino lor capitani, e finalmente lo Sforza; e
poi risalgono a lor monti saccheggiando per via. Cosí il Moro, traditore
tradito, fu preso, tratto a Francia e tenuto poi dieci anni al castello di
Loches, finché vi morí disprezzato, dimenticato. E Milano e il ducato
ridiventarono francesi tranquillamente per parecchi anni.—Intanto Luigi
XII aveva giá apparecchiato l’acquisto di Napoli in questo modo. Addí 11
novembre 1500, in Granata erasi firmato un trattato tra lui e Ferdinando
il cattolico, parente e protettore di Federigo III, re di Napoli; ed eravisi
concertato che i francesi assalirebbono il Regno, che gli spagnuoli
accorrerebbero a difenderlo, e che prima d’incontrarsi, lo spartirebbono.
Certo costoro eran contemporanei non del tutto indegni del Moro, di
Alessandro VI e di Cesare Borgia. Effettuossi l’accordo. Nella state del
1501, entrarono per la frontiera settentrionale del Regno il duca di
Nemours co’ francesi, e per le Calabrie Gonzalvo il Gran capitano, che
macchiò sue glorie in quest’infamie. Federigo il misero re, tradito e ridotto
agli ultimi, scelse capitolar co’ nemici vecchi anziché con gli amici
traditori, e diessi in mano a’ francesi che il trassero a Torsi dove morí nel
1504. Cosí finí il primo regno indipendente di Napoli; e andò a riunirsi a

Sicilia, nella servitú straniera, per due secoli e mezzo.—Intanto, e
naturalmente, disputaronsi i ladroni per le spoglie. Corso appena un anno
[1502], ruppesi guerra tra francesi e spagnuoli. Combattutosi variamente
dapprima, furono sconfitti i francesi a Seminara e Cerignola [aprile 1503].
E sceso un altro esercito francese, fu vinto pur esso al Garigliano al fine
del medesimo anno dal Gran capitano; e tutto il Regno rimase fin d’allora
spagnuolo.—Nell’agosto era morto papa Borgia. La brevitá cosí sovente
tormentante di questo sunto ci serve qui, dispensandoci dal dire le
dissolutezze, le rapine, i tradimenti, i veleni, le crudeltá di tutta quella
famiglia. Tanto piú che tutto ciò fu bensí il sommo della perversitá di quei
tempi perversi, ma non ne fu mutato essenzialmente né durevolmente
quasi nulla in Italia. Fu progetto di Alessandro e del figlio distrurre i
signorotti, i vicari pontefici che signoreggiavano nelle cittá della Chiesa, i
Colonna ed Orsini intorno a Roma, i Varani in Camerino, i Freducci in
Fermo, i Trinci in Foligno, i La Rovere in Sinigaglia ed Urbino, i Baglioni
in Perugia, i Vitelli in Cittá di Castello, gli Sforza in Pesaro, i Malatesta in
Rimini, i Riario in Imola, gli Ordelaffi in Forlí, i Manfredi in Faenza, i
Bentivoglio in Bologna e gli Estensi in Ferrara. Cesare Borgia doveva
rimanerne duca di Romagna. Ma con tutte le loro male arti sofferte od
aiutate dalle potenze italiane e straniere, a che riuscirono? Assassinarono
signorotti, riunirono poche signorie, e non durò il ducato. E meraviglia
che Machiavello ed altri di que’ tempi ammirasser costoro. Se non che, la
Dio mercé, e che che si dica, anche la scienza politica è progredita d’allora
in poi: il Machiavello de’ nostri tempi ha professato che le scelleratezze
sogliono essere non solamente delitti, ma errori. Cosí fosse ben imparato e
tenuto fermo in Italia. Dicesi che Alessandro VI istituisse la censura
ecclesiastica de’ libri [1 giugno 1502]; ma ei non fece che applicarla a’
libri stampati. E il fatto sta che ella esistette sempre, ed esiste in
qualunque chiesa, anche acattolica, voglia mantenere i suoi dommi. La
cattiva imitazione, poi, delle censure politiche nacque molto piú tardi.
Dicesi morisse Alessandro di un veleno apparecchiato a’ suoi nemici, e
preso da lui e dal figliuolo che ne rimase infermo, e incapace di
provvedere ai fatti suoi durante la vacanza della Sede.—La sola buona
opera italiana di questo tempo, fu la guerra sostenuta da Venezia contro a’
turchi nel Friuli, in Grecia, in mare, dal 1499 al 1503, in che fecesi pace.
S’allega a scusa dell’aver cosí mal provveduto Venezia in quegli anni
all’indipendenza d’Italia; non serve ad ogni modo per gli anni addietro.
Tutti gli italiani furono colpevoli, in somma, che la penisola libera di
stranieri (e si può dir degli imperatori stessi) dieci anni addietro, fosse ora
tutta occupata da essi, salvo Venezia, Toscana, e gli Stati del papa.

4. Pio III, Giulio II [1503-1513].—Succeduti al pontificato Pio III
(Piccolomini) per pochi giorni, e poi Giulio II per dieci anni, non so s’io
dica che peggiorassero o migliorassero le condizioni nostre. Giulio II era
quel Giuliano della Rovere, che egli pure aveva chiamati, condotti i
francesi a Napoli. Fatto papa, chiamò francesi e tedeschi contra Venezia.
Poi, avutone quel che voleva, si ravvide, bandí una guerra che chiamò
«santa» contra francesi, bandí la cacciata de’ barbari; e per aver esso,
ultimo de’ papi, fatto udir questo gran grido, il nome di lui riman glorioso
e caro nelle memorie italiane. E noi siamo stanchi di severitá, noi
rispettiamo le tradizioni nazionali, e cerchiam le occasioni di lodare.—
Alla morte d’Alessandro molte delle cittá tenute dal Borgia si sollevarono.
Giulio II, appena salito al trono, gli domandò le rimanenti; e rifiutato, lo
fece prendere, gli fece firmare per forza la consegna, e lo rilasciò poi. Ed
egli se n’andò a Napoli, vi fu di nuovo imprigionato da Gonsalvo e
mandato a Spagna; dove fuggito di prigione, fu a Navarra, e finí poi piú
degnamente che non meritava, coll’armi in mano [1507].—Nel 1506
venne il re cattolico al regno di Napoli, e ne ritrasse il Gran capitano che
l’avea conquistato, che sopravvisse poi in Ispagna in ozio e disfavore.
Giulio II continuò ciò che era buono de’ disegni de’ Borgia, la riduzione
de’ signorotti; e vi riuscí meglio, ridusseli quasi tutti, gli stessi Baglioni di
Perugia, e i Bentivoglio di Bologna [1506]. Ma per compiere la riunione
dello Stato rimanevano a riprendersi a Venezia Ravenna e Cervia usurpate
fin dal secolo scorso, Faenza, Rimini e Forlimpopoli ultimamente tra il
rovinar di Cesare Borgia. A ciò si volse tutto papa Giulio; aveva ogni
ragione, ma proseguilla in mal modo, aggiugnendosi all’ire o piuttosto alle
ambizioni di Luigi XII e di Massimiliano. Fin dal 1504 avean costoro
firmato un’alleanza per dividersi gli Stati continentali di Venezia, ma non
n’avean fatto nulla, finché non vi s’aggiunsero papa Giulio per riaver
quelle cittá, e il re cattolico, gli Estensi e i Gonzaga per simili contese od
ambizioni di vicinato. Fu firmata la famosa e brutta lega a Cambrai [10
dicembre 1508]. Primi ad assalire furono i francesi coll’armi dal Milanese;
seguí il papa coll’armi e con le scomuniche. Contro ai primi stavano a
capo d’un esercito di quaranta e piú mila uomini l’Alviano ed il Pitigliano,
due de’ piú abili condottieri o piuttosto (perché giá non erano piú cosí
indipendenti come gli antichi) capitani d’Italia. Furono vinti da Luigi XII e
trenta mila francesi ad Agnadello [14 maggio 1509]; Luigi XII prese in
pochi dí tutta la parte sua convenuta. Accorsero quindi tutti gli altri, e
presero facilmente le loro. E allora Venezia ridotta all’estremo fu
veramente magnanima, prese uno di quei partiti semplici che sono non
solamente piú gloriosi sempre, ma sovente piú felici che non le destrezze.

Sciolse dall’obbedienza tutti i suoi sudditi di terraferma; ed essi si difesero
meglio, e, quando occupati, si sollevarono secondo le occorrenze per se
stessi. E Giulio II, satisfatto di riavere sue cittá, si staccò primo dalla lega,
fece sua pace addí 24 febbraio 1510; e si rivolse contra i francesi,
nascostamente prima, apertamente tra breve. Per ciò chiamò nuovi
stranieri, gli svizzeri; i quali, capitanati da un cardinale guerriero e
vescovo di Sion, piombarono sul Milanese a mezzo quell’anno, mentre si
avanzavano i papalini da Modena, e riavanzavano i veneziani da Verona.
Ma i francesi stavano sulle guardie; e poco mancò non prendessero papa
Giulio, che, guerriero anch’esso, stava lí vicino a Bologna, e che per la
breccia entrò poco appresso alla Mirandola. E qui pure v’ha chi ammira, e
vorrebbe imitazioni; non io, che credo un papa debba restar papa, ed
abbia altri modi di cacciar barbari dal suo paese. Furono rotti i pontifici a
Casalecchio [21 maggio 1511]; ma Giulio perdurò, s’inaspri, fece [5
ottobre] un’altra lega santa con Venezia, svizzeri, Spagna e fino
Inghilterra contra Francia. Massimiliano solo rimaneva con questa, ma
inutile. In tali strettezze usarono i due l’arme antica contro ai papi,
convocarono un concilio a Pisa. Ma un forte esercito spagnuolo sotto al
Cardona veniva in aiuto a Giulio II, ed assediava Bologna tornata
nuovamente a’ Bentivogli [21 maggio 1511]; e i veneziani riprendean
Brescia. Allora apparí per poco una vera meraviglia di arte e virtú
militare, un predecessore de’ grandi capitani moderni, Gastone di Foix,
nipote del re di Francia, giovane di ventidue anni. Il quale, appena ebbe
preso il comando, che ficcatosi in mezzo ai due eserciti nemici, e
piombando or sull’uno or sull’altro, addí 7 febbraio respinse gli spagnuoli
da Bologna, addí 19 ruppe i veneziani e riprese Brescia, e ritornò quindi
sull’esercito spagnuolo e papalino, e li sconfisse a Ravenna [11 aprile]. Ma
ivi morí, immortalatosi in pochi mesi. E allora precipitarono i francesi.
Massimiliano lasciò passare ventimila svizzeri che scendean alleati a’
veneziani; Spagna e Inghilterra assaliron Francia; Luigi XII richiamò il suo
esercito dal Milanese; Massimiliano Sforza, figlio del Moro, fu fatto duca a
Milano; in giugno si sollevò Genova e cacciò i francesi. Cosí, toltene
alcune castella, furon questi cacciati di tutt’Italia. Ma eran tutt’altro che
cacciati tutti i barbari. Abbondavano spagnuoli, tedeschi e svizzeri, e
tiranneggiavan cosí, che, per dar loro una ricompensa delle vittorie
procacciate alla lega, fu loro abbandonata una delle piu nobili cittá e
potenze italiane, Firenze.—Questa fin da poco dopo la vittoria degli
«arrabbiati» contro al Savonarola s’era riordinata e posata sotto l’autoritá
d’un solo; e (tanto era impossibile oramai un governo piú repubblicano)
sotto un Soderini, gonfaloniero a vita [1502], che avea poi retto con

bontá, semplicitá, mediocritá. Machiavello era uno de’ due segretari o
ministri principali di lui. Tra tutti ed a forza di trattare, barcheggiare,
scivolare, eran riusciti ad ottenere che si lasciasse lor riprendere la
desiderata Pisa, e l’avean presa [1509]. Ma, se non esclusivamente, eran
pur sempre rimasti stretti con Francia; ed ora i vittoriosi di Francia le
posero una multa per quella fedeltá. Que’ mercatanti repubblicani che
aveano avute velleitá ma non volontá di ordinar armi proprie, secondo il
consiglio di Machiavello, e che eran poi gretti e stretti in fatto di danari,
ricusarono, indugiarono. Vengono i Medici, cioè (morto giá Piero da
parecchi anni) Giuliano e il cardinal Giovanni, ed offrono pagar la multa
se fosser fatti signori della cittá. Cardona accetta, varca Appennino,
prende, saccheggia Prato; e i fiorentini, spaventati, si sollevano, cacciano
Soderini, e accettan i Medici [settembre 1512]. Governarono insieme
Giuliano e il cardinal Giovanni. Ma questi per poco; ché, morto papa
Giulio addí 21 febbraio 1513, gli successe esso il cardinal Giovanni [11
marzo] con quel nome di Leone X, che, a torto od a ragione, è forse il piú
noto, il piú popolare fra quelli di quanti papi furon mai.
5. Leone X [1513-1521].—Le nature facili, liete, pompose, leggiere,
trascurate od anche un po’ spensierate, sogliono piú che l’altre trovar
fortuna in vita, e gloria dopo morte. Tal fu, tal sorte ebbe Leone X, del
resto non gran principe politico ed ancor meno gran papa. Nato nel 1475,
cresciuto tra l’eleganze, le colture, le magnificenze del palazzo Medici e
della villa di Careggi; tra Ficino, Poliziano, Pico della Mirandola,
Michelangelo, e una turba di minori, ma simili; cardinale a tredici anni;
fuoruscitosi in sui diciannove, ma nella porpora, ed ora a Roma, ora alle
corti dentro e fuori d’Italia; in colti ozi durante Alessandro VI; poi negli
affari, nelle legazioni sotto Giulio II; prigione alla battaglia di Ravenna,
ma in breve liberato, ed autor principale della restaurazione di sua casa in
sua bella cittá; l’elezione, l’assunzione, l’incoronazione di lui furono veri
trionfi. Dopo Alessandro VI, troppo scellerato per essere nemmeno stato
protettor d’arti o di lettere, dopo Giulio II, fiero, iroso in queste stesse
protezioni, pensi ognuno qual gioia dovesse or sorgere in quella turba di
letterati ed artisti che, quasi ballerine tra guerrieri, si frammettevano
allora ai feroci invasori, ai cupi politici, ed ai dolenti popoli d’Italia.
Quella lieta turba non si vuol perder di memoria mai da chiunque voglia
farsi un’idea adeguata di questi tempi singolarissimi. Certo in quelli di
PericIe, d’Augusto, né di Ludovico XIV, non fu, o almeno non durò, niun
siffatto contrasto di feste e di dolori. Qui la patria era in mano a stranieri;

e il principe successor d’Alessandro III e di Giulio II pensava ai nepoti, ai
Medici, a far loro Stati in Firenze ed Urbino. Qui sorgeva il sommo degli
eresiarchi stati mai dopo Ario; e il pontefice pensava che fosse un
frataccio peggio che il Savonarola, e che finirebbe come lui; e proseguiva
in quell’abbellir Roma, in quell’edificare, e scolpire, e dipingere, e fare
scrivere e rappresentare commedie che avevano scandalezzata la rozza
Germania.
Insomma,
moralmente,
politicamente
e
religiosamente
parlando, non sarebbe troppo il dire che fu un vero baccanale di tutte le
colture; e se scendessimo ai particolari di sua incoronazione, o, peggio, di
ciò che fu allora scritto, rappresentato, dipinto o scolpito in Vaticano, ei
parrebbe forse dimostrato a ciascuno. """
# Starte den Prozess
translate_and_save(MEIN_TEXT)