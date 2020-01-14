#Importing Important Libaries
import csv
#X-Axis Data
years = [1901, 1906, 1911, 1916, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
#Y-Axis Data
sydney_pop = [496990, 559800, 656800, 764600, 885000, 912750, 934540, 952620, 974540, 996100, 1019860, 1044770, 1066400, 1176900, 1190590, 1200830, 1213880, 1237130, 1241900, 1245590, 1251150, 1256500, 1263220, 1274930, 1294080, 1331290, 1363010, 1402790, 1433000, 1456350, 1475150, 1489620, 1503740, 1530060, 1557220, 1574880, 1579790, 1576480, 1863161, 1906340, 1949400, 1996010, 2043200, 2085790, 2132680, 2303807, 2353280, 2397620, 2441570, 2491320, 2542207, 2583650, 2630690, 2690580, 2751830, 3015900, 3053900, 3079600, 3108500, 3129000, 3143800, 3168100, 3197700, 3226800, 3257500, 3279539, 3319302, 3351105, 3385017, 3424594, 3471489, 3526166, 3587999, 3621273, 3642763, 3672914, 3708310, 3728426, 3758844, 3802786, 3856646, 3905123, 3945098, 3991974, 4041730, 4102580, 4135637, 4162593, 4184763, 4217563, 4256161, 4325525, 4409562, 4492380, 4555516, 4608949, 4677196, 4757364, 4841349, 4930189, 5024923]
melbourne_pop = [501580, 530660, 600160, 695640, 763000, 800520, 831060, 861760, 889720, 917080, 945500, 971000, 990650, 1006000, 999650, 995600, 993800, 995800, 1000000, 1008300, 1016500, 1024300, 1035600, 1050700, 1083000, 1114900, 1143900, 1156600, 1168900, 1180200, 1189800, 1228300, 1247800, 1272300, 1302200, 1330800, 1359100, 1388800, 1524111, 1575300, 1629400, 1677100, 1726100, 1777700, 1831100, 1984936, 2029240, 2077560, 2130980, 2180800, 2230793, 2283000, 2331000, 2389700, 2447600, 2606900, 2651600, 2686400, 2722400, 2746200, 2764100, 2782600, 2800700, 2816300, 2835500, 2857907, 2887744, 2916524, 2942787, 2970627, 2996733, 3035229, 3075917, 3121026, 3163590, 3194707, 3217776, 3231603, 3243516, 3268881, 3304912, 3336088, 3368966, 3407286, 3450077, 3500249, 3545579, 3594031, 3641951, 3697372, 3760760, 3841760, 3931438, 4031787, 4105857, 4169366, 4265843, 4370067, 4476030, 4586012, 4714387]
brisbane_pop = [120650, 132470, 143510, 168390, 205980, 217710, 230200, 235690, 245020, 253220, 258620, 264030, 275780, 284760, 279950, 283440, 298140, 301250, 304930, 306150, 313430, 318430, 325890, 330000, 335520, 344230, 353590, 370460, 384040, 393580, 399530, 404640, 414500, 429530, 444650, 453660, 469000, 488000, 502320, 515000, 527500, 543000, 555000, 567000, 578000, 692924, 706679, 721756, 740306, 759085, 778193, 793960, 810410, 829070, 847220, 957900, 977800, 1000700, 1024900, 1042100, 1058100, 1073700, 1090100, 1105900, 1126100, 1154705, 1190830, 1213607, 1227454, 1245078, 1265114, 1286535, 1313047, 1349743, 1382453, 1411773, 1435614, 1464508, 1494739, 1527888, 1560296, 1584086, 1607386, 1632209, 1660663, 1693556, 1735730, 1780650, 1823496, 1866210, 1908265, 1958907, 2012204, 2068479, 2108348, 2147436, 2196288, 2241944, 2281740, 2318653, 2362672]
adelaide_pop = [162200, 175640, 199760, 223720, 255000, 259590, 267570, 274520, 283540, 294710, 305510, 314330, 316390, 310920, 310530, 310460, 311840, 313000, 314000, 315000, 317000, 318000, 321500, 323000, 330000, 350000, 355000, 360000, 365000, 372000, 380000, 388000, 399000, 415500, 433500, 447500, 464000, 476000, 483508, 499100, 517900, 533600, 547400, 562300, 576600, 659316, 673750, 695700, 720900, 748350, 771561, 784450, 795000, 809650, 826850, 883900, 894900, 905500, 915500, 933200, 940100, 951300, 960700, 964800, 970900, 979895, 989474, 1001244, 1013446, 1024259, 1034960, 1043949, 1054472, 1067855, 1080060, 1093525, 1100976, 1103868, 1108322, 1111739, 1116237, 1122518, 1129489, 1136427, 1142726, 1148006, 1154981, 1162250, 1168541, 1177345, 1189243, 1204210, 1219523, 1237354, 1253097, 1264091, 1277850, 1289696, 1302079, 1313419, 1324057]
perth_pop = [70700, 95870, 111400, 124110, 152000, 155590, 161770, 173770, 180790, 183500, 188260, 195080, 200520, 206310, 211640, 215800, 214880, 209000, 211000, 214000, 217000, 220000, 223000, 227000, 230000, 234000, 239000, 245000, 253000, 260000, 268000, 276000, 283000, 296000, 313000, 322000, 335000, 345000, 348647, 360000, 372000, 382000, 391000, 401000, 409000, 475576, 491300, 509200, 525800, 540700, 559298, 583800, 611800, 642800, 671900, 744600, 767200, 782000, 803700, 826400, 845700, 866100, 884500, 899200, 917000, 941479, 973542, 998576, 1017871, 1041608, 1075959, 1106882, 1139494, 1178097, 1207701, 1226115, 1247523, 1266704, 1289836, 1316658, 1343355, 1366707, 1388787, 1411070, 1432115, 1455361, 1474536, 1496016, 1520232, 1544977, 1576912, 1628467, 1682860, 1739342, 1781132, 1833567, 1892862, 1943855, 1973923, 1998937, 2019263]
hobart_pop = [36060, 39230, 40200, 40260, 50000, 53870, 54420, 54980, 55540, 56100, 56680, 57250, 57840, 58430, 59020, 59620, 60230, 62150, 62610, 63620, 64830, 66490, 67700, 68580, 69370, 69390, 69930, 70970, 72230, 73790, 75510, 76534, 78310, 80580, 83680, 87190, 90650, 93280, 95206, 97428, 99536, 103944, 105611, 109756, 111851, 130236, 132790, 135320, 137310, 139400, 141311, 143390, 145830, 149090, 151230, 157100, 158300, 160100, 162400, 165200, 166900, 168300, 169600, 171000, 172300, 174120, 175226, 176477, 178844, 181228, 182846, 183837, 184413, 185982, 189070, 191648, 193505, 194906, 195899, 196758, 197124, 196892, 196533, 196618, 196966, 197403, 197726, 199788, 201771, 203288, 204753, 206649, 209166, 212085, 214669, 216273, 217670, 219315, 221365, 223502, 225913]
darwin_pop = [0, 0, 1082, 0, 0, 1399, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1566, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2538, 0, 0, 0, 0, 0, 0, 8071, 8600, 8900, 0, 0, 0, 0, 15477, 0, 0, 17800, 0, 21671, 23400, 26300, 29300, 32900, 39000, 43200, 46900, 51700, 35300, 47300, 51000, 54900, 57200, 59600, 62078, 67052, 70807, 74959, 79114, 82814, 85014, 84009, 84588, 85694, 86414, 87834, 89570, 91424, 94429, 97247, 100518, 102395, 104345, 106412, 108280, 108679, 108433, 109211,  1113880,  113461, 116935, 121210, 125315, 127829, 129106, 133105, 138471, 141169, 144914, 147102]
canberra_pop = [0,0, 0,0,0, 1150, 1500, 2000, 2600, 3500, 4900, 6150, 6640, 6880, 7290, 7050, 7030, 7325, 7500, 7700, 8030, 8410, 9827, 10800, 12000, 13300, 12650, 11650, 12450, 13250, 14100, 15156, 18040, 19640, 22080, 23140, 24530, 26710, 28277, 30710, 33100, 35827, 39061, 43973, 50237, 56449, 63821, 70775, 77644, 85690, 93314, 100938, 109550, 119235, 129000, 151169, 159792, 173306, 186241, 199007, 207740, 213688, 217981, 220797, 224291, 226821, 232304, 238261, 244409, 250705, 258246, 264801, 271439, 275728, 281492, 288586, 294230, 299114, 302194, 305838, 309629, 310533, 311532, 314171, 317235, 321538, 324627, 327357, 328940, 331399, 335170, 342644, 348368, 354785, 361766, 367985, 376539, 383257, 388799, 395813, 403104]
capital_cities = [1388180, 1533670, 1752912, 2016720, 2310980, 2402579, 2481060, 2555340, 2631750, 2704210, 2779330, 2852610, 2914220, 3050200, 3058670, 3072800, 3099800, 3127221, 3141940, 3160360, 3187940, 3212130, 3246737, 3285010, 3353970, 3457110, 3537080, 3617470, 3688620, 3749170, 3802090, 3880788, 3944390, 4043610, 4156330, 4239170, 4322070, 4394270, 4853301, 4992478, 5137736, 5271481, 5407372, 5547519, 5689468, 6318721, 6450860, 6607931, 6792310, 6945345, 7138348, 7296588, 7460580, 7659425, 7858530, 8556469, 8706692, 8834506, 8975341, 9076407, 9173740, 9274788, 9376181, 9461997, 9563191, 9676544, 9835474, 9966601, 10084787, 10217213, 10368161, 10532413, 10710790, 10884292, 11032823, 11165682, 11285768, 11378699, 11484774, 11624977, 11785446, 11922465, 12050186, 12194100, 12347924, 12526973, 12677495, 12831118, 12978905, 13149542, 13344725, 13625097, 13934331, 14261527, 14508214, 14736773, 15037353, 15343969, 15626454, 15911439, 16221421]
rest_nsw = [878465, 961818, 1042576, 1120451, 1206722, 1218940, 1246977, 1270259, 1298483, 1326240, 1356818, 1388885, 1416729, 1342793, 1355763, 1365484, 1377851, 1376474, 1394563, 1412482, 1431170, 1455043, 1473971, 1491485, 1496868, 1481766, 1485130, 1467921, 1468039, 1476648, 1487242, 1513014, 1544566, 1619746, 1683837, 1739792, 1788196, 1832529, 1560368, 1584409, 1604857, 1628959, 1648754, 1674044, 1699773, 1614694, 1633668, 1652378, 1666345, 1684118, 1695694, 1711589, 1728635, 1750608, 1770500, 1709603, 1741206, 1762298, 1785553, 1803016, 1815788, 1833788, 1856090, 1884330, 1914027, 1955350, 1984278, 2001854, 2017712, 2039918, 2060037, 2090570, 2119310, 2155010, 2191258, 2225817, 2249512, 2266629, 2285975, 2302774, 2319815, 2341144, 2360701, 2383129, 2404828, 2427769, 2445170, 2458122, 2465972, 2475643, 2486529, 2508631, 2533899, 2561375, 2588776, 2609580, 2627048, 2646668, 2667004, 2685979, 2707935]
rest_vic = [708320, 689172, 739733, 709023, 764909, 750207, 759213, 763695, 767431, 766971, 766487, 770832, 771096, 772269, 792955, 807970, 819587, 828417, 836660, 833295, 833107, 832691, 835499, 832433, 831918, 831525, 818658, 825016, 829054, 834907, 849969, 834409, 860325, 896584, 934982, 968738, 1007619, 1027235, 928230, 941929, 964068, 979157, 992382, 1008205, 1026289, 945430, 953818, 963281, 974539, 983569, 989424, 991340, 993180, 995343, 997336, 994452, 1009654, 1021253, 1033326, 1041241, 1046326, 1054764, 1063059, 1070106, 1078803, 1089010, 1105126, 1119178, 1133705, 1149441, 1164123, 1174882, 1186652, 1199138, 1215002, 1225666, 1232441, 1231163, 1229473, 1228779, 1230072, 1233209, 1238004, 1245176, 1253988, 1263366, 1272195, 1279778, 1285198, 1291874, 1300506, 1311762, 1324937, 1340147, 1355244, 1368451, 1385248, 1402602, 1418887, 1436310, 1458785]
rest_qld = [386071, 406503, 479613, 508636, 544644, 548014, 552179, 566154, 577064, 591622, 603866, 612355, 615097, 617376, 636786, 646286, 640957, 647894, 654914, 665147, 669548, 676150, 679633, 690095, 695932, 694241, 684335, 684124, 684215, 691284, 697301, 708178, 724044, 740789, 760768, 784618, 802256, 810420, 815939, 835017, 854091, 870085, 884199, 901237, 917927, 834590, 844303, 856111, 870392, 885449, 896131, 906022, 918586, 934017, 945523, 893585, 920678, 951251, 983440, 1009262, 1034275, 1056139, 1081947, 1108871, 1139835, 1190503, 1233756, 1268675, 1296405, 1326140, 1359481, 1388572, 1426860, 1477894, 1516830, 1549178, 1587584, 1631677, 1671827, 1709492, 1742896, 1771331, 1797098, 1821727, 1848795, 1877913, 1917393, 1962471, 2006474, 2052284, 2099727, 2152111, 2207301, 2260292, 2296396, 2329342, 2372399, 2410880, 2437913, 2459039, 2482480]
rest_sa = [201803, 194777, 219632, 218118, 236006, 242152, 244032, 247692, 251406, 252338, 255415, 255300, 256197, 262053, 263937, 266619, 267453, 269746, 270489, 271762, 272770, 273797, 274342, 276313, 269056, 256366, 255978, 256027, 258030, 258882, 260418, 266632, 271615, 280118, 289343, 296285, 304570, 309665, 313586, 320467, 330657, 339566, 349403, 358598, 368720, 312171, 313746, 315041, 317120, 319221, 323423, 325330, 326811, 329683, 331137, 316214, 319728, 322975, 326038, 332064, 333970, 334819, 335505, 336309, 337497, 338874, 341634, 344531, 346602, 346938, 347590, 348815, 350437, 351174, 351996, 352774, 354466, 354764, 354767, 353601, 352842, 353140, 353781, 354507, 354777, 355455, 356586, 358149, 359648, 361459, 363286, 366409, 369142, 371548, 374225, 375523, 378875, 381792, 384866, 387249, 388786]
rest_wa = [122901, 159303, 182523, 182770, 179323, 180958, 183774, 183089, 187534, 194027, 196973, 204817, 214101, 220327, 219970, 217886, 221440, 231642, 232729, 235623, 237200, 240542, 243684, 245380, 244076, 239213, 237655, 233264, 231775, 230088, 228973, 232762, 238999, 248184, 259649, 268339, 277935, 286743, 291124, 297115, 302529, 305605, 308565, 311070, 313080, 271174, 274662, 279144, 282643, 284825, 288802, 295379, 303242, 312046, 319454, 309234, 314817, 319041, 323898, 328548, 332642, 338266, 343351, 347411, 352068, 358577, 365357, 370474, 373366, 376956, 383060, 389366, 395673, 400337, 405348, 409952, 411021, 412018, 414813, 419408, 424851, 431634, 437653, 442866, 446978, 450913, 453976, 456725, 459310, 466230, 473669, 477672, 488840, 500908, 509713, 519842, 532645, 543089, 543685, 541735, 536715]
rest_tas = [139173, 146242, 152725, 155343, 162752, 164806, 165348, 165431, 164132, 163264, 160895, 161901, 162479, 164848, 166277, 168844, 170377, 170025, 169028, 169803, 170943, 173080, 174419, 174676, 174632, 172745, 172507, 173283, 174659, 176490, 179060, 180544, 182896, 186482, 192222, 199003, 205649, 210800, 213546, 216664, 218934, 222186, 227455, 229620, 232059, 220104, 222878, 225407, 227001, 228505, 230125, 231854, 233819, 235803, 236490, 240973, 242008, 242987, 243751, 244888, 245414, 246732, 248042, 249756, 251290, 253104, 254619, 256328, 258916, 261600, 263627, 265389, 266735, 269276, 273118, 275154, 276474, 277081, 277600, 277757, 278481, 278016, 276897, 276412, 276157, 276265, 276426, 278746, 281407, 282914, 284549, 286613, 289402, 292268, 294178, 295210, 294054, 292916, 292256, 291615, 291601]
rest_nt = [0,0, 2151,0,0, 2360,0, 0,0, 0,0, 0,0, 0,0, 0,0, 3261,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 8354,0, 0,0, 0,0,0, 8398, 9610, 10656,0, 0,0,0, 29004,0,0, 33663,0, 34833, 38436, 41237, 43662, 45911, 46735, 48881, 50227, 51224, 57569, 50928, 52938, 55080, 56949, 58645, 60538, 63262, 65109, 67195, 69422, 71607, 73191, 75017, 76591, 78034, 79079, 80712, 82138, 83484, 85173, 87269, 89237, 90510, 91667, 92737, 93463, 93572, 93292, 93452, 94517, 95596, 96813, 98664, 100712, 101949, 102186, 102810, 103251, 101725, 99778, 98576]
rest_act = [0,0, 0,0,0, 1433, 1438, 1506, 1520, 1558, 1650, 1535, 1513, 1614, 1723, 1593, 1551, 1622, 1970, 1939, 2278, 2571, 1735, 1767, 1753, 1722, 1739, 1737, 1755, 1762, 1767, 1749, 1751, 1746, 1744, 1752, 1830, 1935, 2038, 2040, 2035, 2038, 2106, 2097, 2131, 2379, 2352, 2625, 2689, 2775, 2718, 2540, 2545, 2427, 2468,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, ]
rest_states = [2436733, 2557815, 2818953, 2894341, 3094356, 3108870, 3152961, 3197826, 3247570, 3296020, 3342104, 3395625, 3437212, 3381280, 3437411, 3474682, 3499216, 3529081, 3560353, 3590051, 3617016, 3653874, 3683283, 3712149, 3714235, 3677578, 3656002, 3641372, 3647527, 3670061, 3704730, 3745642, 3824196, 3973649, 4122545, 4258527, 4388055, 4479327, 4133229, 4207251, 4287827, 4347596, 4412864, 4484871, 4559979, 4229546, 4245427, 4293987, 4374392, 4388462, 4461150, 4502490, 4548055, 4603589, 4648819, 4510796, 4596972, 4670032, 4747230, 4816588, 4859343, 4917446, 4983074, 5053732, 5132165, 5245956, 5348032, 5426149, 5493901, 5570415, 5649525, 5730785, 5820684, 5929420, 6031586, 6117620, 6192210, 6255470, 6317939, 6376984, 6436226, 6497711, 6554644, 6615484, 6678260, 6745144, 6815318, 6887283, 6951461, 7024921, 7103862, 7200011, 7312185, 7427250, 7520481, 7600134, 7693079, 7781198, 7846336, 7901705, 7964878]

"""#Opens csv File
with open('capitals.csv') as csvfile:
    # Reads csv File
    readCSV = csv.reader(csvfile,  delimiter=', ')
    #for each row in csv file
    for row in readCSV:
        print(row[2])



#Opens csv File
with open('auspop.csv') as csvfile:
    # Reads csv File
    readCSV = csv.reader(csvfile,  delimiter=', ')
    #for each row in csv file
    for row in readCSV:
        #add column 6 to the years list
        years.append(row[6])
        #add column -3 to the births list
        aus_births.append(row[-3])
"""
#reout put data per into new csv file
with open('capitals_best.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(years, sydney_pop, melbourne_pop, brisbane_pop, adelaide_pop, perth_pop, hobart_pop, darwin_pop, canberra_pop, capital_cities, rest_nsw, rest_vic, rest_qld, rest_sa, rest_wa, rest_tas, rest_nt, rest_act, rest_states))