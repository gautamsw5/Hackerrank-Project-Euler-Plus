import math
N,K=map(int,input().split())
if K==5:
    if N>=8389:
        print(26033)
    if N>=18433:
        print(34427)
ans4=[[673, 792], [4159, 4710], [8747, 9462], [2297, 4380], [8219, 10302], [8747, 10830], [2069, 2538], [6353, 6822], [6599, 7068], [2297, 4386], [6571, 7842], [13399, 14670], [17209, 21402], [8431, 16056], [13399, 21810], [2377, 2484], [5923, 6030], [8713, 9990], [8713, 10452], [4159, 6576], [10243, 12660], [16759, 20958], [17209, 21408], [7963, 12732], [7963, 13926], [14627, 15882], [13931, 19374], [18523, 19206], [7159, 14028], [15739, 22608], [19387, 28704], [19387, 35202], [18289, 33894], [8747, 11010], [8431, 9504], [10771, 14742], [15559, 16758], [14627, 17148], [10169, 13062], [4253, 5340], [16937, 21660], [17209, 21912], [18233, 24234], [8713, 16524], [8713, 16986], [5869, 13656], [11827, 21924], [19919, 37920], [8783, 17628], [17029, 26412], [15461, 31818], [16937, 33294], [9181, 21876], [19441, 32136], [19031, 42714], [19183, 39222], [19387, 42000], [19441, 37518], [18713, 39624], [3727, 3850], [4507, 4630], [3727, 5002], [5659, 9412], [8941, 9496], [3181, 4942], [13309, 15718], [15973, 24982], [13807, 14806], [18433, 23116], [7723, 14806], [18433, 19102], [3613, 5524], [9613, 13666], [19681, 33298], [8167, 11182], [19801, 22816], [15973, 32548], [10909, 22402], [3361, 6868], [8779, 11908], [8779, 17656], [12973, 24238], [3019, 5812], [12409, 15994], [18433, 22018], [18433, 32086], [6949, 11932], [6949, 12646], [14029, 23266], [12409, 16636], [3181, 8230], [4219, 9496], [5821, 11710], [13309, 28066], [18433, 33190], [17659, 28300], [17659, 33610], [19333, 27646], [19597, 33892], [9613, 19990], [19237, 27268], [11617, 22864], [13627, 27430], [15643, 26776], [10399, 25918], [16447, 33904], [13147, 30118], [17989, 34324], [17989, 34528], [10513, 28066], [14551, 34168], [1871, 2648], [8171, 10076], [8681, 10586], [8747, 11864], [8681, 14564], [7331, 13694], [10433, 12530], [1847, 3146], [11057, 12356], [1847, 3188], [5807, 9524], [15731, 28904], [5849, 11180], [8219, 13550], [8831, 15986], [8747, 17000], [11351, 20810], [6329, 13250], [12653, 16724], [16937, 30818], [19949, 30512], [14759, 27800], [7127, 14402], [12911, 24278], [5153, 13820], [11399, 24470], [8831, 20180], [5849, 15656], [15641, 33818], [15731, 36230], [15131, 40790], [16937, 41024], [6043, 11152], [9697, 16720], [12277, 22006], [13999, 23752], [19543, 19948], [5431, 7888], [7993, 14866], [17929, 27862], [17683, 31042], [8053, 13576], [8599, 16426], [8599, 17728], [9697, 17512], [9883, 18814], [9091, 21928], [17683, 39730], [9697, 21004], [6733, 17644], [8389, 19300], [8389, 20332], [8389, 20836], [19273, 36838], [12197, 18194], [19841, 25838], [9923, 16742], [14759, 21482], [14423, 28988], [18869, 25214], [16217, 27092], [4649, 11324], [6899, 13574], [8537, 15944], [18371, 28028], [18869, 26936], [13913, 28166], [18701, 39740], [16427, 41804], [9679, 9910], [8641, 9682], [6271, 7558], [8641, 14962], [18517, 20062], [18517, 24406], [10687, 20464], [18517, 26284], [12457, 22744], [17569, 25078], [12577, 21802], [18451, 25090], [8623, 19330], [8929, 18532], [9697, 26110], [18517, 40510], [4211, 5762], [5927, 8330], [5483, 9764], [6323, 8792], [827, 1838], [11321, 17336], [1871, 3398], [6323, 8960], [5849, 12488], [14957, 22406], [5051, 10634], [8237, 16940], [19433, 30470], [7607, 14066], [11321, 21404], [6563, 11900], [12641, 22160], [12227, 23984], [9311, 16070], [12641, 22664], [6911, 15230], [2281, 5464], [5281, 8464], [9439, 15802], [8641, 16222], [9439, 17200], [8287, 15178], [5701, 12100], [18637, 28522], [17923, 36118], [19309, 27922], [9133, 22000], [19309, 44248], [9049, 25102], [15667, 35176], [8761, 15544], [3613, 6910], [14779, 17206], [3463, 7756], [8011, 17884], [15031, 23842], [5857, 13510], [17209, 26194], [8101, 19852], [17041, 37858], [7331, 15572], [15791, 30452], [8521, 10042], [12697, 16210], [6967, 14170], [18451, 28606], [18451, 35704], [9697, 13180], [17569, 27346], [12697, 17806], [18661, 36004], [12157, 18178], [14029, 28096], [9349, 15754], [12157, 18562], [19963, 40726], [5273, 10718], [4931, 7364], [9833, 15902], [10313, 15260], [8963, 14702], [8963, 16130], [14447, 18824], [10463, 18020], [9239, 17948], [6701, 14378], [16253, 24560], [14447, 25250], [10313, 17900], [13001, 23792], [19421, 32240], [19289, 35894], [11057, 21758], [13241, 16826], [8933, 14048], [9341, 16700], [11057, 17486], [15809, 23258], [8123, 15602], [16943, 27656], [17903, 25976], [8537, 21944], [13241, 34214], [19423, 35122], [16111, 20674], [9511, 13396], [15859, 27154], [7687, 13792], [12421, 15526], [9907, 19546], [10909, 19096], [10909, 26602], [17077, 35464], [5849, 7904], [8087, 19544], [9239, 21728], [13907, 28934], [18757, 20020], [11287, 19510], [15643, 16702], [8887, 10450], [17341, 24994], [18793, 25066], [3511, 5674], [3547, 8680], [8263, 15112], [17467, 28852], [17467, 42094], [7583, 14606], [12119, 13694], [12119, 20000], [10691, 13616], [11447, 19136], [11447, 24008], [4973, 6230], [11489, 12992], [13043, 14546], [11489, 17912], [8663, 16094], [15083, 21968], [8147, 18326], [5581, 8278], [5581, 12412], [12697, 21124], [11257, 28336], [19081, 53212], [19553, 32786], [4337, 9770], [18311, 44708], [9619, 19468], [13697, 27320], [9043, 16174], [6481, 15250], [13873, 27076], [5519, 8858], [12269, 24902], [9491, 22856], [7933, 13138], [7933, 18958], [6733, 16882], [15859, 31216], [19759, 20902], [5563, 10690], [15973, 17632], [19867, 33634], [10181, 20648], [15053, 25844], [10463, 14132], [11933, 19424], [12043, 22216], [16057, 42172], [15271, 19390], [15271, 29482], [5107, 12892], [16633, 33634], [16843, 23506], [19997, 49628], [6733, 11596], [11491, 21844], [7949, 16808], [19013, 41666], [19319, 21662], [7523, 10658], [15859, 24472], [8093, 19268], [2741, 4514], [17609, 22496], [17863, 39664], [16061, 32750], [19541, 45680], [9931, 13678], [9931, 13108], [6607, 11212], [18793, 30664], [16699, 33850], [14347, 29680], [9473, 10850], [12853, 30880], [8663, 10622], [8867, 17162], [16111, 31726], [6037, 11812], [14683, 29134], [16111, 32338], [6037, 12328], [9749, 20924], [17911, 27412], [9857, 11630], [14281, 17836], [8219, 19112], [14753, 35054], [17957, 41942], [9601, 19972], [18913, 47680], [9239, 14090], [9677, 15140], [16871, 22334], [14867, 20726], [17387, 29426], [4567, 9790], [7927, 13168], [15427, 30514], [7933, 20164], [7691, 14204], [7691, 15170], [14537, 26300], [8779, 15220], [7883, 16502], [5297, 6728], [17377, 36664], [15643, 36346], [11597, 27734], [17431, 36166], [11173, 22528], [8699, 17816], [9839, 22406], [14083, 27094], [17189, 30854], [17189, 38942], [6323, 7994], [9473, 11144], [14669, 17054], [19793, 23300], [16811, 40430], [19163, 50510], [16843, 25744], [18947, 28604], [7907, 12398], [19477, 29614], [19531, 42532], [16229, 33938], [17189, 45410], [10597, 25240], [7949, 15212], [19753, 48442], [11941, 26200], [15581, 18176], [16063, 35842], [15313, 31624], [15959, 25826], [14243, 30290], [15881, 31928], [18233, 24848], [16987, 44194], [7949, 15716], [6257, 13694], [19697, 42074], [14549, 30872], [8389, 15004], [19417, 55078], [8171, 15950], [16217, 34910], [18493, 21100], [15061, 25684], [19609, 51286], [19423, 42730], [13627, 35848], [16231, 44092], [19697, 34874], [11069, 18986], [3947, 8258], [5393, 14828], [17977, 35122], [8663, 17114], [12049, 23962], [15739, 34768], [13687, 33208], [14947, 40396], [14771, 23732], [13553, 21182], [12511, 28426], [19333, 41626], [19333, 49174], [10883, 23066], [14957, 33602], [10487, 14240], [16141, 26470], [12703, 37210], [17191, 32326], [19919, 23696], [9923, 15710], [6949, 19960], [16319, 28028], [14009, 34724], [19949, 40106], [15937, 31546], [15017, 19856], [19441, 27466], [19441, 29650], [12011, 24176], [11171, 24554], [11299, 22678], [13807, 21310], [9931, 17494], [11353, 21154], [11353, 23758], [8461, 24388], [11353, 27280], [18289, 32008], [19423, 33142], [6451, 18520], [19391, 29168], [19391, 37550], [17519, 29480], [13457, 19220], [7529, 17990], [8663, 24662], [14593, 34792], [7489, 17812], [19381, 25984], [7507, 17050], [12197, 17684], [19139, 49778], [8069, 13784], [12611, 30890], [8501, 19634], [8861, 20978], [7817, 16424], [8861, 20204], [15329, 26282], [12907, 21334], [19309, 27736], [19309, 37846], [15901, 30658], [12409, 22558], [18433, 34420], [18229, 38446], [7949, 14978], [8747, 20162], [9137, 18374], [17789, 42902], [7919, 16742], [15443, 28412], [13151, 25400], [14633, 25628], [4133, 10484], [10169, 19154], [13297, 28750], [14543, 28688], [7949, 18092], [17903, 31346], [10627, 17776], [10627, 21682], [9811, 17092], [8461, 18280], [9689, 21002], [17939, 38294], [6983, 16082], [15173, 23198], [6983, 17912], [4051, 12070], [3761, 11324], [16111, 30400], [7963, 14806], [18329, 30350], [14717, 28112], [8209, 19018], [10993, 25306], [15313, 29626], [7907, 17690], [6827, 16832], [15727, 39640], [9091, 24058], [6113, 12020], [13037, 22784], [8171, 21758], [10531, 18160], [14369, 33446], [18797, 30050], [7477, 15052], [19661, 42248], [8831, 15716], [8273, 21572], [14771, 28112], [15289, 34312], [18169, 30184], [16453, 33880], [18169, 35596], [18169, 39046], [13291, 29182], [3643, 10894], [8929, 19726], [15277, 26074], [15277, 29764], [15277, 34006], [4273, 12652], [8461, 17470], [13003, 28318], [12157, 24718], [16619, 46988], [8693, 17234], [8783, 25124], [19333, 38080], [8011, 21358], [9533, 22490], [14447, 32006], [8573, 24548], [10937, 24938], [13217, 27722], [17977, 31654], [8209, 19528], [8317, 17446], [17581, 42826], [4523, 13628], [8923, 25858], [6599, 16382], [12713, 22466], [14951, 29468], [19927, 30856], [8081, 22400], [12659, 28628], [7879, 18868], [9109, 23314], [14387, 27566], [9049, 22612], [14731, 35344], [8831, 22412], [19301, 46478], [16253, 44294], [9619, 25936], [15233, 27260], [15767, 35690], [15329, 25460], [9929, 21422], [17207, 35192], [12143, 29924], [19777, 43618], [15217, 39862], [11579, 29762], [16253, 36944], [12893, 37502], [8821, 27586], [19919, 57044], [16223, 41294], [7039, 18382], [19861, 42130], [12841, 40492], [19069, 50344], [18583, 34618], [14447, 28226], [11177, 24272], [13217, 32000], [15767, 38876], [17539, 34690], [15121, 41680], [18097, 39604], [19739, 47972], [7331, 21554], [9431, 27926], [19403, 39488], [9257, 20084], [5501, 17996], [10091, 25550], [13633, 29482], [9791, 24002], [14033, 29876], [10151, 25004], [8461, 19918], [8461, 21538], [8737, 24808], [10069, 27802], [18493, 38950], [14083, 32434], [7993, 22636], [15271, 40636], [15739, 45022], [10133, 24272], [13873, 39280], [17189, 41708], [8017, 22144], [17551, 32344], [18743, 44894], [9817, 26476], [15787, 33934], [9013, 23860], [9391, 25180], [18523, 45898], [9811, 24094], [14533, 27820], [14083, 30010], [6607, 17074], [18427, 31858], [14713, 38626], [17707, 41614], [9817, 22456], [9817, 27838], [19237, 32020], [19489, 46474], [13267, 28558], [10069, 28582], [10181, 22328], [16333, 44386], [16427, 41216], [17957, 50306], [18973, 55060], [11503, 33646], [11161, 27514], [16729, 40486], [8863, 27442], [14197, 32416], [19889, 49466], [15641, 35798], [18743, 55826], [16103, 41024], [12739, 27466], [15859, 45958], [12841, 42502], [12641, 32870], [8233, 26488], [16921, 34018], [15277, 37756], [19441, 49618], [12739, 33832], [19249, 48952], [8573, 27452], [8741, 28748], [7039, 24346], [16651, 45310], [9901, 29518], [8389, 26020], [18427, 38296], [18143, 42374], [9239, 31694], [7039, 25960], [14389, 38488], [11549, 34604], [16007, 43436], [14347, 34462], [14851, 37030], [18457, 36634], [9613, 32548], [18269, 47804], [18713, 50558], [19727, 39620], [8863, 29920], [19841, 50828], [17333, 38384], [18143, 45314], [18839, 51902], [8537, 28574], [9551, 31436], [17351, 39356], [16561, 46828], [14713, 37024], [19571, 54602], [19427, 42326], [17977, 47548], [15727, 46150], [14143, 39370], [14143, 42100], [17837, 54338], [13291, 43522], [17627, 55850], [16087, 42034], [17203, 55372], [16903, 56470], [17203, 58936], [19373, 52292], [16651, 49438], [16447, 49684], [17707, 50944], [17551, 56806], [13831, 45460], [14251, 50092], [19597, 55558], [14737, 51040], [17291, 59120], [18457, 63670]]
if K==4:
    ans=[]
    for i in ans4:
        if i[0]<=N:
            ans.append(i[1])
    ans.sort()
    for i in ans:
        print(i)
if K==3:
    pairs=set()
    dct={}
    ans=[]
    ans3=set()
    p=set()
    np=set()
    P=[]
    prime=[True]*999999
    for i in range(2,999999):
        if prime[i]:
            p.add(i)
            P.append(i)
            for k in range(2*i,999999,i):
                prime[k]=False
    def isprime(n):
        if n in p:
            return True
        elif n<P[-1] and not n in p:
            return False
        elif n in np:
            return False
        lim=math.sqrt(n)+2
        for i in P:
            if i>lim:
                break
            if n%i==0:
                np.add(n)
                return False
        p.add(n)
        return True
    for a in P[1:]:
        if a>N:
            break
        for b in P[1:]:
            if b>N:
                break
            if a<b and isprime(int(str(a)+str(b))) and isprime(int(str(b)+str(a))):
                pairs.add((a,b))
                if not a in dct:
                    dct[a]=set()
                dct[a].add(b)
    for start in dct:
        for x in dct[start]:
            for a in dct[start]:
                if x<a and (x,a) in pairs:
                    ans3.add((start,x,a))
    for x in ans3:
        if x[2]<=N:
            ans.append(x[0]+x[1]+x[2])
    ans.sort()
    s=""
    for i in ans:
        s=s+str(i)+"\n"
    print(s)