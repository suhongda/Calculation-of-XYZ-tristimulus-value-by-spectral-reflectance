import numpy as np

O2 = np.array([[380, 0.00137, 0.000039, 0.00645],
 [381, 0.0015, 0.0000428, 0.00708],
 [382, 0.00164, 0.0000469, 0.00775],
 [383, 0.0018, 0.0000516, 0.0085],
 [384, 0.002, 0.0000572, 0.00941],
 [385, 0.00224, 0.000064, 0.01055],
 [386, 0.00254, 0.0000723, 0.01197],
 [387, 0.00289, 0.0000822, 0.01366],
 [388, 0.0033, 0.0000935, 0.01559],
 [389, 0.00375, 0.0001061, 0.01773],
 [390, 0.00424, 0.00012, 0.02005],
 [391, 0.00476, 0.000135, 0.02251],
 [392, 0.00533, 0.0001515, 0.0252],
 [393, 0.00598, 0.0001702, 0.02828],
 [394, 0.00674, 0.0001918, 0.0319],
 [395, 0.00765, 0.000217, 0.03621],
 [396, 0.00875, 0.0002469, 0.04144],
 [397, 0.01003, 0.0002812, 0.0475],
 [398, 0.01142, 0.0003185, 0.05412],
 [399, 0.01287, 0.0003573, 0.061],
 [400, 0.01431, 0.000396, 0.06785],
 [401, 0.0157, 0.0004337, 0.07449],
 [402, 0.01715, 0.000473, 0.08136],
 [403, 0.01878, 0.0005179, 0.08915],
 [404, 0.02075, 0.0005722, 0.09854],
 [405, 0.02319, 0.00064, 0.1102],
 [406, 0.02621, 0.0007246, 0.12461],
 [407, 0.02978, 0.0008255, 0.1417],
 [408, 0.03388, 0.0009412, 0.1613],
 [409, 0.03847, 0.00107, 0.18326],
 [410, 0.04351, 0.00121, 0.2074],
 [411, 0.049, 0.00136, 0.23369],
 [412, 0.05502, 0.00153, 0.26261],
 [413, 0.06172, 0.00172, 0.29477],
 [414, 0.06921, 0.00194, 0.3308],
 [415, 0.07763, 0.00218, 0.3713],
 [416, 0.08696, 0.00245, 0.41621],
 [417, 0.09718, 0.00276, 0.46546],
 [418, 0.10841, 0.00312, 0.51969],
 [419, 0.12077, 0.00353, 0.57953],
 [420, 0.13438, 0.004, 0.6456],
 [421, 0.14936, 0.00455, 0.71848],
 [422, 0.1654, 0.00516, 0.79671],
 [423, 0.18198, 0.00583, 0.87785],
 [424, 0.19861, 0.00655, 0.95944],
 [425, 0.21477, 0.0073, 1.03905],
 [426, 0.23019, 0.00809, 1.11537],
 [427, 0.24488, 0.00891, 1.1885],
 [428, 0.25878, 0.00977, 1.25812],
 [429, 0.27181, 0.01066, 1.32393],
 [430, 0.2839, 0.0116, 1.3856],
 [431, 0.29494, 0.01257, 1.44264],
 [432, 0.3049, 0.01358, 1.4948],
 [433, 0.31379, 0.01463, 1.54219],
 [434, 0.32165, 0.01572, 1.58488],
 [435, 0.3285, 0.01684, 1.62296],
 [436, 0.33435, 0.01801, 1.6564],
 [437, 0.33921, 0.01921, 1.6853],
 [438, 0.34312, 0.02045, 1.70987],
 [439, 0.34613, 0.02172, 1.73038],
 [440, 0.34828, 0.023, 1.74706],
 [441, 0.3496, 0.02429, 1.76004],
 [442, 0.35015, 0.02561, 1.76962],
 [443, 0.35001, 0.02696, 1.77626],
 [444, 0.34929, 0.02835, 1.78043],
 [445, 0.34806, 0.0298, 1.7826],
 [446, 0.34637, 0.03131, 1.78297],
 [447, 0.34426, 0.03288, 1.7817],
 [448, 0.34181, 0.03452, 1.7792],
 [449, 0.33909, 0.03623, 1.77587],
 [450, 0.3362, 0.038, 1.77211],
 [451, 0.3332, 0.03985, 1.76826],
 [452, 0.33004, 0.04177, 1.76404],
 [453, 0.32664, 0.04377, 1.75894],
 [454, 0.32289, 0.04584, 1.75247],
 [455, 0.3187, 0.048, 1.7441],
 [456, 0.31403, 0.05024, 1.73356],
 [457, 0.30888, 0.05257, 1.72086],
 [458, 0.30329, 0.05498, 1.70594],
 [459, 0.29726, 0.05746, 1.68874],
 [460, 0.2908, 0.06, 1.6692],
 [461, 0.28397, 0.0626, 1.64753],
 [462, 0.27672, 0.06528, 1.62341],
 [463, 0.26892, 0.06804, 1.59602],
 [464, 0.26042, 0.07091, 1.56453],
 [465, 0.2511, 0.0739, 1.5281],
 [466, 0.24085, 0.07702, 1.48611],
 [467, 0.22985, 0.08027, 1.43952],
 [468, 0.21841, 0.08367, 1.38988],
 [469, 0.20681, 0.08723, 1.33874],
 [470, 0.19536, 0.09098, 1.28764],
 [471, 0.18421, 0.09492, 1.23742],
 [472, 0.17333, 0.09905, 1.18782],
 [473, 0.16269, 0.10337, 1.13876],
 [474, 0.15228, 0.10788, 1.09015],
 [475, 0.1421, 0.1126, 1.0419],
 [476, 0.13218, 0.11753, 0.9942],
 [477, 0.12257, 0.12267, 0.94735],
 [478, 0.11328, 0.12799, 0.90145],
 [479, 0.1043, 0.13345, 0.85662],
 [480, 0.09564, 0.13902, 0.81295],
 [481, 0.0873, 0.14468, 0.77052],
 [482, 0.07931, 0.15047, 0.72944],
 [483, 0.07172, 0.15646, 0.68991],
 [484, 0.06458, 0.16272, 0.6521],
 [485, 0.05795, 0.1693, 0.6162],
 [486, 0.05186, 0.17624, 0.58233],
 [487, 0.04628, 0.18356, 0.55042],
 [488, 0.04115, 0.19127, 0.52034],
 [489, 0.03641, 0.19942, 0.49197],
 [490, 0.03201, 0.20802, 0.46518],
 [491, 0.02792, 0.21712, 0.43992],
 [492, 0.02414, 0.22673, 0.41618],
 [493, 0.02069, 0.23686, 0.39388],
 [494, 0.01754, 0.24748, 0.37295],
 [495, 0.0147, 0.2586, 0.3533],
 [496, 0.01216, 0.27018, 0.33486],
 [497, 0.00992, 0.28229, 0.31755],
 [498, 0.00797, 0.29505, 0.30134],
 [499, 0.0063, 0.30858, 0.28617],
 [500, 0.0049, 0.323, 0.272],
 [501, 0.00378, 0.3384, 0.25882],
 [502, 0.00295, 0.35469, 0.24648],
 [503, 0.00242, 0.3717, 0.23477],
 [504, 0.00224, 0.38929, 0.22345],
 [505, 0.0024, 0.4073, 0.2123],
 [506, 0.00293, 0.42563, 0.20117],
 [507, 0.00384, 0.44431, 0.19012],
 [508, 0.00517, 0.46339, 0.17923],
 [509, 0.00698, 0.48294, 0.16856],
 [510, 0.0093, 0.503, 0.1582],
 [511, 0.01215, 0.52357, 0.14814],
 [512, 0.01554, 0.54451, 0.13838],
 [513, 0.01948, 0.56569, 0.12899],
 [514, 0.02399, 0.58697, 0.12008],
 [515, 0.0291, 0.6082, 0.1117],
 [516, 0.03481, 0.62935, 0.1039],
 [517, 0.04112, 0.65031, 0.09667],
 [518, 0.04799, 0.67088, 0.08998],
 [519, 0.05538, 0.69084, 0.08385],
 [520, 0.06327, 0.71, 0.07825],
 [521, 0.07164, 0.72819, 0.07321],
 [522, 0.08046, 0.74546, 0.06868],
 [523, 0.08974, 0.76197, 0.06457],
 [524, 0.09946, 0.77784, 0.06079],
 [525, 0.1096, 0.7932, 0.05725],
 [526, 0.12017, 0.80811, 0.0539],
 [527, 0.13111, 0.8225, 0.05075],
 [528, 0.14237, 0.83631, 0.04775],
 [529, 0.15385, 0.84949, 0.0449],
 [530, 0.1655, 0.862, 0.04216],
 [531, 0.17726, 0.87381, 0.03951],
 [532, 0.18914, 0.88496, 0.03694],
 [533, 0.20117, 0.89549, 0.03446],
 [534, 0.21337, 0.90544, 0.03209],
 [535, 0.22575, 0.91485, 0.02984],
 [536, 0.23832, 0.92373, 0.02771],
 [537, 0.25107, 0.93209, 0.02569],
 [538, 0.26399, 0.93992, 0.02379],
 [539, 0.2771, 0.94723, 0.02199],
 [540, 0.2904, 0.954, 0.0203],
 [541, 0.30389, 0.96026, 0.01872],
 [542, 0.31757, 0.96601, 0.01724],
 [543, 0.33144, 0.97126, 0.01586],
 [544, 0.34548, 0.97602, 0.01458],
 [545, 0.3597, 0.9803, 0.0134],
 [546, 0.37408, 0.98409, 0.01231],
 [547, 0.38864, 0.98742, 0.0113],
 [548, 0.40338, 0.99031, 0.01038],
 [549, 0.41831, 0.99281, 0.00953],
 [550, 0.43345, 0.99495, 0.00875],
 [551, 0.4488, 0.99671, 0.00804],
 [552, 0.46434, 0.9981, 0.00738],
 [553, 0.48006, 0.99911, 0.00679],
 [554, 0.49597, 0.99975, 0.00624],
 [555, 0.51205, 1, 0.00575],
 [556, 0.5283, 0.99986, 0.0053],
 [557, 0.54469, 0.9993, 0.0049],
 [558, 0.56121, 0.99833, 0.00453],
 [559, 0.57782, 0.9969, 0.0042],
 [560, 0.5945, 0.995, 0.0039],
 [561, 0.61122, 0.9926, 0.00362],
 [562, 0.62798, 0.98974, 0.00337],
 [563, 0.64476, 0.98644, 0.00314],
 [564, 0.66157, 0.98272, 0.00293],
 [565, 0.6784, 0.9786, 0.00275],
 [566, 0.69524, 0.97408, 0.00259],
 [567, 0.71206, 0.96917, 0.00244],
 [568, 0.72883, 0.96386, 0.00231],
 [569, 0.74552, 0.95813, 0.0022],
 [570, 0.7621, 0.952, 0.0021],
 [571, 0.77854, 0.94545, 0.00202],
 [572, 0.79483, 0.9385, 0.00195],
 [573, 0.81093, 0.93116, 0.00189],
 [574, 0.82682, 0.92346, 0.00184],
 [575, 0.8425, 0.9154, 0.0018],
 [576, 0.85793, 0.90701, 0.00177],
 [577, 0.87308, 0.89828, 0.00174],
 [578, 0.88789, 0.8892, 0.00171],
 [579, 0.90232, 0.87978, 0.00168],
 [580, 0.9163, 0.87, 0.00165],
 [581, 0.9298, 0.85986, 0.00161],
 [582, 0.9428, 0.84939, 0.00156],
 [583, 0.95528, 0.83862, 0.00151],
 [584, 0.96722, 0.82758, 0.00146],
 [585, 0.9786, 0.8163, 0.0014],
 [586, 0.98939, 0.80479, 0.00134],
 [587, 0.99955, 0.79308, 0.00127],
 [588, 1.00909, 0.78119, 0.0012],
 [589, 1.01801, 0.76915, 0.00115],
 [590, 1.0263, 0.757, 0.0011],
 [591, 1.03398, 0.74475, 0.00107],
 [592, 1.04099, 0.73242, 0.00105],
 [593, 1.04719, 0.72, 0.00104],
 [594, 1.05247, 0.7075, 0.00102],
 [595, 1.0567, 0.6949, 0.001],
 [596, 1.05979, 0.68222, 0.0009686],
 [597, 1.0618, 0.66947, 0.0009299],
 [598, 1.06281, 0.65667, 0.0008869],
 [599, 1.06291, 0.64384, 0.0008426],
 [600, 1.0622, 0.631, 0.0008],
 [601, 1.06074, 0.61816, 0.000761],
 [602, 1.05844, 0.60531, 0.0007237],
 [603, 1.05522, 0.59248, 0.0006859],
 [604, 1.05098, 0.57964, 0.0006454],
 [605, 1.0456, 0.5668, 0.0006],
 [606, 1.03904, 0.55396, 0.0005479],
 [607, 1.03136, 0.54114, 0.0004916],
 [608, 1.02267, 0.52835, 0.0004354],
 [609, 1.01305, 0.51563, 0.0003835],
 [610, 1.0026, 0.503, 0.00034],
 [611, 0.99137, 0.49047, 0.0003073],
 [612, 0.97933, 0.47803, 0.0002832],
 [613, 0.96649, 0.46568, 0.0002654],
 [614, 0.95285, 0.4534, 0.0002518],
 [615, 0.9384, 0.4412, 0.00024],
 [616, 0.92319, 0.42908, 0.0002295],
 [617, 0.90724, 0.41704, 0.0002206],
 [618, 0.8905, 0.40503, 0.000212],
 [619, 0.87292, 0.39303, 0.0002022],
 [620, 0.85445, 0.381, 0.00019],
 [621, 0.83508, 0.36892, 0.0001742],
 [622, 0.81495, 0.35683, 0.0001556],
 [623, 0.79419, 0.34478, 0.000136],
 [624, 0.77295, 0.33282, 0.0001169],
 [625, 0.7514, 0.321, 0.0001],
 [626, 0.72958, 0.30934, 0.0000861],
 [627, 0.70759, 0.29785, 0.0000746],
 [628, 0.6856, 0.28659, 0.000065],
 [629, 0.66381, 0.27562, 0.0000569],
 [630, 0.6424, 0.265, 0.00005],
 [631, 0.62151, 0.25476, 0.0000442],
 [632, 0.60111, 0.24489, 0.0000395],
 [633, 0.58111, 0.23533, 0.0000357],
 [634, 0.5614, 0.22605, 0.0000326],
 [635, 0.5419, 0.217, 0.00003],
 [636, 0.5226, 0.20816, 0.0000277],
 [637, 0.50355, 0.19955, 0.0000256],
 [638, 0.48474, 0.19116, 0.0000236],
 [639, 0.46619, 0.18297, 0.0000218],
 [640, 0.4479, 0.175, 0.00002],
 [641, 0.42986, 0.16722, 0.0000181],
 [642, 0.4121, 0.15965, 0.0000162],
 [643, 0.39464, 0.15228, 0.0000142],
 [644, 0.37753, 0.14513, 0.0000121],
 [645, 0.3608, 0.1382, 0.00001],
 [646, 0.34446, 0.1315, 0.00000773],
 [647, 0.32852, 0.12502, 0.0000054],
 [648, 0.31302, 0.11878, 0.0000032],
 [649, 0.298, 0.11277, 0.00000133],
 [650, 0.2835, 0.107, 0],
 [651, 0.26954, 0.10148, 0],
 [652, 0.25612, 0.09619, 0],
 [653, 0.24319, 0.09112, 0],
 [654, 0.23073, 0.08626, 0],
 [655, 0.2187, 0.0816, 0],
 [656, 0.2071, 0.07712, 0],
 [657, 0.19592, 0.07283, 0],
 [658, 0.18517, 0.06871, 0],
 [659, 0.17483, 0.06477, 0],
 [660, 0.1649, 0.061, 0],
 [661, 0.15537, 0.0574, 0],
 [662, 0.14623, 0.05396, 0],
 [663, 0.13749, 0.05067, 0],
 [664, 0.12915, 0.04755, 0],
 [665, 0.1212, 0.04458, 0],
 [666, 0.11364, 0.04176, 0],
 [667, 0.10647, 0.03909, 0],
 [668, 0.09969, 0.03656, 0],
 [669, 0.09333, 0.0342, 0],
 [670, 0.0874, 0.032, 0],
 [671, 0.0819, 0.02996, 0],
 [672, 0.0768, 0.02808, 0],
 [673, 0.07208, 0.02633, 0],
 [674, 0.06769, 0.02471, 0],
 [675, 0.0636, 0.0232, 0],
 [676, 0.05981, 0.0218, 0],
 [677, 0.05628, 0.0205, 0],
 [678, 0.05297, 0.01928, 0],
 [679, 0.04982, 0.01812, 0],
 [680, 0.04677, 0.017, 0],
 [681, 0.04378, 0.0159, 0],
 [682, 0.04088, 0.01484, 0],
 [683, 0.03807, 0.01381, 0],
 [684, 0.0354, 0.01283, 0],
 [685, 0.0329, 0.01192, 0],
 [686, 0.03056, 0.01107, 0],
 [687, 0.02838, 0.01027, 0],
 [688, 0.02634, 0.00953, 0],
 [689, 0.02445, 0.00885, 0],
 [690, 0.0227, 0.00821, 0],
 [691, 0.02108, 0.00762, 0],
 [692, 0.0196, 0.00709, 0],
 [693, 0.01824, 0.00659, 0],
 [694, 0.01699, 0.00614, 0],
 [695, 0.01584, 0.00572, 0],
 [696, 0.01479, 0.00534, 0],
 [697, 0.01383, 0.005, 0],
 [698, 0.01295, 0.00468, 0],
 [699, 0.01213, 0.00438, 0],
 [700, 0.01136, 0.0041, 0],
 [701, 0.01063, 0.00384, 0],
 [702, 0.00994, 0.00359, 0],
 [703, 0.00929, 0.00335, 0],
 [704, 0.00868, 0.00313, 0],
 [705, 0.00811, 0.00293, 0],
 [706, 0.00758, 0.00274, 0],
 [707, 0.00709, 0.00256, 0],
 [708, 0.00663, 0.00239, 0],
 [709, 0.0062, 0.00224, 0],
 [710, 0.00579, 0.00209, 0],
 [711, 0.00541, 0.00195, 0],
 [712, 0.00505, 0.00182, 0],
 [713, 0.00472, 0.0017, 0],
 [714, 0.0044, 0.00159, 0],
 [715, 0.00411, 0.00148, 0],
 [716, 0.00383, 0.00138, 0],
 [717, 0.00358, 0.00129, 0],
 [718, 0.00333, 0.0012, 0],
 [719, 0.00311, 0.00112, 0],
 [720, 0.0029, 0.00105, 0],
 [721, 0.0027, 0.0009766, 0],
 [722, 0.00252, 0.0009111, 0],
 [723, 0.00235, 0.0008501, 0],
 [724, 0.0022, 0.0007932, 0],
 [725, 0.00205, 0.00074, 0],
 [726, 0.00191, 0.0006901, 0],
 [727, 0.00178, 0.0006433, 0],
 [728, 0.00166, 0.0005995, 0],
 [729, 0.00155, 0.0005585, 0],
 [730, 0.00144, 0.00052, 0],
 [731, 0.00134, 0.0004839, 0],
 [732, 0.00125, 0.0004501, 0],
 [733, 0.00116, 0.0004183, 0],
 [734, 0.00108, 0.0003887, 0],
 [735, 0.0009999, 0.0003611, 0],
 [736, 0.0009287, 0.0003354, 0],
 [737, 0.0008624, 0.0003114, 0],
 [738, 0.0008008, 0.0002892, 0],
 [739, 0.0007434, 0.0002685, 0],
 [740, 0.0006901, 0.0002492, 0],
 [741, 0.0006405, 0.0002313, 0],
 [742, 0.0005945, 0.0002147, 0],
 [743, 0.0005519, 0.0001993, 0],
 [744, 0.0005124, 0.000185, 0],
 [745, 0.000476, 0.0001719, 0],
 [746, 0.0004425, 0.0001598, 0],
 [747, 0.0004115, 0.0001486, 0],
 [748, 0.000383, 0.0001383, 0],
 [749, 0.0003566, 0.0001288, 0],
 [750, 0.0003323, 0.00012, 0],
 [751, 0.0003098, 0.0001119, 0],
 [752, 0.0002889, 0.0001043, 0],
 [753, 0.0002695, 0.0000973, 0],
 [754, 0.0002516, 0.0000909, 0],
 [755, 0.0002348, 0.0000848, 0],
 [756, 0.0002192, 0.0000792, 0],
 [757, 0.0002045, 0.0000739, 0],
 [758, 0.0001908, 0.0000689, 0],
 [759, 0.0001781, 0.0000643, 0],
 [760, 0.0001662, 0.00006, 0],
 [761, 0.000155, 0.000056, 0],
 [762, 0.0001446, 0.0000522, 0],
 [763, 0.0001349, 0.0000487, 0],
 [764, 0.0001259, 0.0000455, 0],
 [765, 0.0001174, 0.0000424, 0],
 [766, 0.0001096, 0.0000396, 0],
 [767, 0.0001022, 0.0000369, 0],
 [768, 0.0000954, 0.0000345, 0],
 [769, 0.000089, 0.0000322, 0],
 [770, 0.0000831, 0.00003, 0],
 [771, 0.0000775, 0.000028, 0],
 [772, 0.0000723, 0.0000261, 0],
 [773, 0.0000675, 0.0000244, 0],
 [774, 0.0000629, 0.0000227, 0],
 [775, 0.0000587, 0.0000212, 0],
 [776, 0.0000548, 0.0000198, 0],
 [777, 0.0000511, 0.0000185, 0],
 [778, 0.0000477, 0.0000172, 0],
 [779, 0.0000445, 0.0000161, 0],
 [780, 0.0000415, 0.000015, 0]])

O10 = np.array([[380, 0.00016, 0.0000174, 0.0007048],
 [381, 0.0002151, 0.0000233, 0.0009482],
 [382, 0.0002875, 0.0000312, 0.00127],
 [383, 0.000382, 0.0000414, 0.00169],
 [384, 0.0005046, 0.0000546, 0.00223],
 [385, 0.0006624, 0.0000716, 0.00293],
 [386, 0.0008645, 0.0000933, 0.00382],
 [387, 0.00112, 0.0001209, 0.00496],
 [388, 0.00145, 0.0001556, 0.00641],
 [389, 0.00185, 0.0001992, 0.00822],
 [390, 0.00236, 0.0002534, 0.01048],
 [391, 0.00299, 0.0003202, 0.01329],
 [392, 0.00376, 0.0004024, 0.01675],
 [393, 0.00471, 0.0005023, 0.02098],
 [394, 0.00586, 0.0006232, 0.02613],
 [395, 0.00724, 0.0007685, 0.03234],
 [396, 0.0089, 0.0009417, 0.0398],
 [397, 0.01087, 0.00115, 0.04869],
 [398, 0.0132, 0.00139, 0.05921],
 [399, 0.01593, 0.00167, 0.07158],
 [400, 0.01911, 0.002, 0.08601],
 [401, 0.02279, 0.00239, 0.10274],
 [402, 0.02701, 0.00282, 0.122],
 [403, 0.03183, 0.00332, 0.14402],
 [404, 0.03728, 0.00388, 0.16899],
 [405, 0.0434, 0.00451, 0.19712],
 [406, 0.05022, 0.00521, 0.22857],
 [407, 0.05776, 0.00598, 0.26347],
 [408, 0.06604, 0.00683, 0.3019],
 [409, 0.07503, 0.00776, 0.34387],
 [410, 0.08474, 0.00876, 0.38937],
 [411, 0.09504, 0.00982, 0.43797],
 [412, 0.10584, 0.01092, 0.48922],
 [413, 0.11707, 0.01206, 0.5429],
 [414, 0.12868, 0.01324, 0.59881],
 [415, 0.14064, 0.01446, 0.65676],
 [416, 0.15289, 0.01572, 0.71658],
 [417, 0.16542, 0.01702, 0.77812],
 [418, 0.17819, 0.0184, 0.84131],
 [419, 0.19121, 0.01985, 0.90611],
 [420, 0.20449, 0.02139, 0.97254],
 [421, 0.21765, 0.02299, 1.0389],
 [422, 0.23027, 0.0246, 1.1031],
 [423, 0.24231, 0.02621, 1.1651],
 [424, 0.25379, 0.02784, 1.2249],
 [425, 0.26474, 0.0295, 1.2825],
 [426, 0.2752, 0.0312, 1.3382],
 [427, 0.2853, 0.03293, 1.3926],
 [428, 0.29514, 0.03474, 1.4461],
 [429, 0.30487, 0.03665, 1.4994],
 [430, 0.31468, 0.03868, 1.55348],
 [431, 0.32436, 0.04079, 1.6072],
 [432, 0.33357, 0.04295, 1.6589],
 [433, 0.34224, 0.04511, 1.7082],
 [434, 0.35031, 0.04733, 1.7548],
 [435, 0.35772, 0.0496, 1.7985],
 [436, 0.36448, 0.05193, 1.8392],
 [437, 0.37049, 0.05434, 1.8766],
 [438, 0.37573, 0.05682, 1.9105],
 [439, 0.38016, 0.0594, 1.9408],
 [440, 0.38373, 0.06208, 1.96728],
 [441, 0.38633, 0.06474, 1.9891],
 [442, 0.38786, 0.06728, 2.0057],
 [443, 0.3884, 0.06976, 2.0174],
 [444, 0.38798, 0.07222, 2.0244],
 [445, 0.38673, 0.0747, 2.0273],
 [446, 0.3847, 0.07727, 2.0264],
 [447, 0.38201, 0.07998, 2.0223],
 [448, 0.37871, 0.08287, 2.0153],
 [449, 0.37492, 0.086, 2.006],
 [450, 0.3707, 0.08946, 1.9948],
 [451, 0.36609, 0.09295, 1.9814],
 [452, 0.36105, 0.09627, 1.9653],
 [453, 0.35552, 0.09953, 1.9464],
 [454, 0.34949, 0.10283, 1.9248],
 [455, 0.34296, 0.10626, 1.9007],
 [456, 0.33589, 0.1099, 1.8741],
 [457, 0.32828, 0.11384, 1.8451],
 [458, 0.32015, 0.11817, 1.8139],
 [459, 0.31148, 0.12293, 1.7806],
 [460, 0.30227, 0.1282, 1.74537],
 [461, 0.29286, 0.13346, 1.7091],
 [462, 0.2835, 0.13832, 1.6723],
 [463, 0.27404, 0.14304, 1.6347],
 [464, 0.26426, 0.14779, 1.5956],
 [465, 0.25409, 0.15276, 1.5549],
 [466, 0.24339, 0.1581, 1.5122],
 [467, 0.23219, 0.16394, 1.4673],
 [468, 0.22049, 0.17036, 1.4199],
 [469, 0.2082, 0.17743, 1.37],
 [470, 0.19562, 0.18519, 1.31756],
 [471, 0.18303, 0.19303, 1.2624],
 [472, 0.17022, 0.20031, 1.205],
 [473, 0.15735, 0.20716, 1.1466],
 [474, 0.14465, 0.21364, 1.088],
 [475, 0.13235, 0.21994, 1.0302],
 [476, 0.12058, 0.22617, 0.97383],
 [477, 0.10946, 0.23247, 0.91943],
 [478, 0.09904, 0.23902, 0.86746],
 [479, 0.08939, 0.246, 0.81828],
 [480, 0.08051, 0.25359, 0.77212],
 [481, 0.07203, 0.26188, 0.72829],
 [482, 0.06371, 0.27064, 0.68604],
 [483, 0.05569, 0.27964, 0.64553],
 [484, 0.04812, 0.28869, 0.60685],
 [485, 0.04107, 0.29767, 0.57006],
 [486, 0.03464, 0.30647, 0.53522],
 [487, 0.0289, 0.31504, 0.50234],
 [488, 0.02388, 0.32333, 0.4714],
 [489, 0.01963, 0.33137, 0.44239],
 [490, 0.01617, 0.33913, 0.41525],
 [491, 0.0133, 0.34786, 0.39002],
 [492, 0.01076, 0.35833, 0.3664],
 [493, 0.00854, 0.37, 0.34402],
 [494, 0.00666, 0.38246, 0.32269],
 [495, 0.00513, 0.39538, 0.30236],
 [496, 0.00398, 0.40848, 0.28304],
 [497, 0.00324, 0.42159, 0.26482],
 [498, 0.00293, 0.43462, 0.24785],
 [499, 0.00311, 0.4476, 0.23232],
 [500, 0.00382, 0.46078, 0.2185],
 [501, 0.00509, 0.47434, 0.20585],
 [502, 0.00694, 0.4882, 0.1936],
 [503, 0.0093, 0.50234, 0.18174],
 [504, 0.01215, 0.51674, 0.17028],
 [505, 0.01544, 0.53136, 0.15925],
 [506, 0.01916, 0.54619, 0.14867],
 [507, 0.02325, 0.56118, 0.13861],
 [508, 0.02769, 0.57629, 0.1291],
 [509, 0.03244, 0.5915, 0.12022],
 [510, 0.03746, 0.60674, 0.11204],
 [511, 0.04296, 0.62215, 0.10471],
 [512, 0.04911, 0.63783, 0.0982],
 [513, 0.05592, 0.65371, 0.09236],
 [514, 0.06335, 0.66968, 0.08709],
 [515, 0.07136, 0.68566, 0.08225],
 [516, 0.0799, 0.70155, 0.07774],
 [517, 0.08891, 0.71723, 0.07346],
 [518, 0.09829, 0.73257, 0.06927],
 [519, 0.10795, 0.74746, 0.06506],
 [520, 0.11775, 0.76176, 0.06071],
 [521, 0.12784, 0.77534, 0.05646],
 [522, 0.13845, 0.78822, 0.05261],
 [523, 0.14952, 0.80046, 0.04912],
 [524, 0.16104, 0.81214, 0.04595],
 [525, 0.17295, 0.82333, 0.04305],
 [526, 0.18521, 0.83412, 0.04037],
 [527, 0.19775, 0.8446, 0.03784],
 [528, 0.21054, 0.85487, 0.03538],
 [529, 0.22346, 0.86504, 0.03295],
 [530, 0.23649, 0.87521, 0.03045],
 [531, 0.24963, 0.88537, 0.02803],
 [532, 0.26297, 0.89537, 0.02586],
 [533, 0.27652, 0.90515, 0.02392],
 [534, 0.29027, 0.91465, 0.02217],
 [535, 0.30421, 0.92381, 0.02058],
 [536, 0.31836, 0.93255, 0.01913],
 [537, 0.3327, 0.94081, 0.01774],
 [538, 0.34723, 0.94852, 0.0164],
 [539, 0.36193, 0.9556, 0.01506],
 [540, 0.37677, 0.96199, 0.01368],
 [541, 0.39168, 0.96754, 0.01231],
 [542, 0.40659, 0.97223, 0.01106],
 [543, 0.42154, 0.97617, 0.00992],
 [544, 0.43652, 0.97946, 0.00887],
 [545, 0.45158, 0.9822, 0.00792],
 [546, 0.46678, 0.98452, 0.00703],
 [547, 0.48215, 0.98652, 0.00622],
 [548, 0.49774, 0.98832, 0.00545],
 [549, 0.51361, 0.99002, 0.00471],
 [550, 0.52983, 0.99176, 0.00399],
 [551, 0.54644, 0.99353, 0.00329],
 [552, 0.56343, 0.99523, 0.00265],
 [553, 0.58073, 0.99677, 0.00206],
 [554, 0.59829, 0.99809, 0.00153],
 [555, 0.61605, 0.99911, 0.00109],
 [556, 0.63395, 0.99977, 0.000711],
 [557, 0.6519, 1, 0.000407],
 [558, 0.66982, 0.99971, 0.000184],
 [559, 0.68763, 0.99885, 0.000047],
 [560, 0.70522, 0.99734, 0],
 [561, 0.72277, 0.99526, 0],
 [562, 0.74048, 0.99274, 0],
 [563, 0.75827, 0.98975, 0],
 [564, 0.77608, 0.9863, 0],
 [565, 0.79383, 0.98238, 0],
 [566, 0.81144, 0.97798, 0],
 [567, 0.82882, 0.97311, 0],
 [568, 0.84588, 0.96774, 0],
 [569, 0.86252, 0.96189, 0],
 [570, 0.87865, 0.95555, 0],
 [571, 0.89421, 0.9486, 0],
 [572, 0.90921, 0.94098, 0],
 [573, 0.92367, 0.9328, 0],
 [574, 0.93764, 0.92416, 0],
 [575, 0.95116, 0.91517, 0],
 [576, 0.96428, 0.90595, 0],
 [577, 0.97707, 0.89661, 0],
 [578, 0.98959, 0.88725, 0],
 [579, 1.00191, 0.87799, 0],
 [580, 1.01416, 0.86893, 0],
 [581, 1.0265, 0.86016, 0],
 [582, 1.0388, 0.85152, 0],
 [583, 1.051, 0.84296, 0],
 [584, 1.0629, 0.83439, 0],
 [585, 1.0743, 0.82562, 0],
 [586, 1.0852, 0.81676, 0],
 [587, 1.0952, 0.80754, 0],
 [588, 1.1042, 0.79795, 0],
 [589, 1.112, 0.78789, 0],
 [590, 1.11852, 0.77741, 0],
 [591, 1.1238, 0.76649, 0],
 [592, 1.128, 0.75531, 0],
 [593, 1.1311, 0.74384, 0],
 [594, 1.1332, 0.73219, 0],
 [595, 1.1343, 0.72035, 0],
 [596, 1.1343, 0.70828, 0],
 [597, 1.1333, 0.69605, 0],
 [598, 1.1312, 0.68362, 0],
 [599, 1.1281, 0.67105, 0],
 [600, 1.12399, 0.65834, 0],
 [601, 1.1189, 0.64555, 0],
 [602, 1.1129, 0.63272, 0],
 [603, 1.1059, 0.61982, 0],
 [604, 1.098, 0.60689, 0],
 [605, 1.0891, 0.59388, 0],
 [606, 1.0792, 0.58078, 0],
 [607, 1.0684, 0.56765, 0],
 [608, 1.0567, 0.55449, 0],
 [609, 1.044, 0.54123, 0],
 [610, 1.03048, 0.52796, 0],
 [611, 1.016, 0.51463, 0],
 [612, 1.0008, 0.50136, 0],
 [613, 0.98479, 0.48812, 0],
 [614, 0.96808, 0.47494, 0],
 [615, 0.95074, 0.46183, 0],
 [616, 0.9328, 0.44882, 0],
 [617, 0.91434, 0.43592, 0],
 [618, 0.89539, 0.42315, 0],
 [619, 0.87603, 0.41053, 0],
 [620, 0.8563, 0.39806, 0],
 [621, 0.83635, 0.38583, 0],
 [622, 0.81629, 0.37395, 0],
 [623, 0.79605, 0.36231, 0],
 [624, 0.77561, 0.35086, 0],
 [625, 0.75493, 0.33955, 0],
 [626, 0.73399, 0.32831, 0],
 [627, 0.71278, 0.31712, 0],
 [628, 0.69129, 0.30594, 0],
 [629, 0.66952, 0.29474, 0],
 [630, 0.64747, 0.28349, 0],
 [631, 0.62511, 0.27222, 0],
 [632, 0.60252, 0.26099, 0],
 [633, 0.57989, 0.24988, 0],
 [634, 0.55737, 0.23895, 0],
 [635, 0.53511, 0.22825, 0],
 [636, 0.51324, 0.21785, 0],
 [637, 0.49186, 0.20778, 0],
 [638, 0.47108, 0.19807, 0],
 [639, 0.45096, 0.18875, 0],
 [640, 0.43157, 0.17983, 0],
 [641, 0.41287, 0.17128, 0],
 [642, 0.39475, 0.16306, 0],
 [643, 0.37721, 0.15515, 0],
 [644, 0.36019, 0.14754, 0],
 [645, 0.34369, 0.14021, 0],
 [646, 0.32769, 0.13317, 0],
 [647, 0.31217, 0.1264, 0],
 [648, 0.29711, 0.11989, 0],
 [649, 0.2825, 0.11364, 0],
 [650, 0.26833, 0.10763, 0],
 [651, 0.25459, 0.10187, 0],
 [652, 0.2413, 0.09635, 0],
 [653, 0.22848, 0.09106, 0],
 [654, 0.21614, 0.08601, 0],
 [655, 0.2043, 0.08119, 0],
 [656, 0.19295, 0.07658, 0],
 [657, 0.18211, 0.0722, 0],
 [658, 0.17177, 0.06802, 0],
 [659, 0.16192, 0.06405, 0],
 [660, 0.15257, 0.06028, 0],
 [661, 0.14367, 0.0567, 0],
 [662, 0.1352, 0.05329, 0],
 [663, 0.12713, 0.05006, 0],
 [664, 0.11948, 0.047, 0],
 [665, 0.11221, 0.0441, 0],
 [666, 0.10531, 0.04135, 0],
 [667, 0.09879, 0.03875, 0],
 [668, 0.09261, 0.0363, 0],
 [669, 0.08677, 0.03398, 0],
 [670, 0.08126, 0.0318, 0],
 [671, 0.07605, 0.02974, 0],
 [672, 0.07111, 0.02779, 0],
 [673, 0.06645, 0.02596, 0],
 [674, 0.06206, 0.02423, 0],
 [675, 0.05793, 0.0226, 0],
 [676, 0.05405, 0.02108, 0],
 [677, 0.05041, 0.01965, 0],
 [678, 0.04701, 0.01832, 0],
 [679, 0.04382, 0.01707, 0],
 [680, 0.04085, 0.01591, 0],
 [681, 0.03807, 0.01482, 0],
 [682, 0.03547, 0.0138, 0],
 [683, 0.03303, 0.01285, 0],
 [684, 0.03075, 0.01196, 0],
 [685, 0.02862, 0.01113, 0],
 [686, 0.02663, 0.01036, 0],
 [687, 0.02478, 0.00963, 0],
 [688, 0.02305, 0.00896, 0],
 [689, 0.02144, 0.00833, 0],
 [690, 0.01994, 0.00775, 0],
 [691, 0.01854, 0.0072, 0],
 [692, 0.01724, 0.0067, 0],
 [693, 0.01603, 0.00623, 0],
 [694, 0.0149, 0.00579, 0],
 [695, 0.01384, 0.00538, 0],
 [696, 0.01286, 0.00499, 0],
 [697, 0.01195, 0.00464, 0],
 [698, 0.0111, 0.00431, 0],
 [699, 0.01031, 0.004, 0],
 [700, 0.00958, 0.00372, 0],
 [701, 0.00889, 0.00345, 0],
 [702, 0.00826, 0.00321, 0],
 [703, 0.00767, 0.00298, 0],
 [704, 0.00712, 0.00276, 0],
 [705, 0.00661, 0.00256, 0],
 [706, 0.00613, 0.00238, 0],
 [707, 0.00569, 0.00221, 0],
 [708, 0.00528, 0.00205, 0],
 [709, 0.0049, 0.0019, 0],
 [710, 0.00455, 0.00177, 0],
 [711, 0.00423, 0.00164, 0],
 [712, 0.00393, 0.00153, 0],
 [713, 0.00365, 0.00142, 0],
 [714, 0.00339, 0.00132, 0],
 [715, 0.00314, 0.00122, 0],
 [716, 0.00292, 0.00114, 0],
 [717, 0.00271, 0.00105, 0],
 [718, 0.00252, 0.0009801, 0],
 [719, 0.00234, 0.0009107, 0],
 [720, 0.00217, 0.0008462, 0],
 [721, 0.00202, 0.0007863, 0],
 [722, 0.00188, 0.0007307, 0],
 [723, 0.00174, 0.000679, 0],
 [724, 0.00162, 0.000631, 0],
 [725, 0.00151, 0.0005864, 0],
 [726, 0.0014, 0.0005451, 0],
 [727, 0.0013, 0.0005067, 0],
 [728, 0.00121, 0.0004711, 0],
 [729, 0.00112, 0.0004381, 0],
 [730, 0.00104, 0.0004074, 0],
 [731, 0.0009716, 0.000379, 0],
 [732, 0.0009036, 0.0003525, 0],
 [733, 0.0008405, 0.000328, 0],
 [734, 0.0007819, 0.0003052, 0],
 [735, 0.0007275, 0.000284, 0],
 [736, 0.0006769, 0.0002644, 0],
 [737, 0.00063, 0.0002461, 0],
 [738, 0.0005864, 0.0002291, 0],
 [739, 0.0005459, 0.0002134, 0],
 [740, 0.0005083, 0.0001987, 0],
 [741, 0.0004733, 0.0001851, 0],
 [742, 0.0004408, 0.0001725, 0],
 [743, 0.0004106, 0.0001607, 0],
 [744, 0.0003825, 0.0001497, 0],
 [745, 0.0003564, 0.0001396, 0],
 [746, 0.0003321, 0.0001301, 0],
 [747, 0.0003096, 0.0001213, 0],
 [748, 0.0002886, 0.0001131, 0],
 [749, 0.0002691, 0.0001055, 0],
 [750, 0.000251, 0.0000984, 0],
 [751, 0.0002341, 0.0000919, 0],
 [752, 0.0002185, 0.0000857, 0],
 [753, 0.00020391, 0.0000801, 0],
 [754, 0.0001904, 0.0000748, 0],
 [755, 0.0001777, 0.0000698, 0],
 [756, 0.000166, 0.0000652, 0],
 [757, 0.000155, 0.0000609, 0],
 [758, 0.0001448, 0.0000569, 0],
 [759, 0.0001353, 0.0000532, 0],
 [760, 0.0001264, 0.0000497, 0],
 [761, 0.0001181, 0.0000465, 0],
 [762, 0.0001104, 0.0000435, 0],
 [763, 0.0001032, 0.0000406, 0],
 [764, 0.0000964, 0.000038, 0],
 [765, 0.0000902, 0.0000355, 0],
 [766, 0.0000843, 0.0000332, 0],
 [767, 0.0000788, 0.0000311, 0],
 [768, 0.0000737, 0.0000291, 0],
 [769, 0.000069, 0.0000272, 0],
 [770, 0.0000645, 0.0000255, 0],
 [771, 0.0000604, 0.0000239, 0],
 [772, 0.0000565, 0.0000223, 0],
 [773, 0.0000529, 0.0000209, 0],
 [774, 0.0000495, 0.0000196, 0],
 [775, 0.0000463, 0.0000183, 0],
 [776, 0.0000434, 0.0000172, 0],
 [777, 0.0000406, 0.0000161, 0],
 [778, 0.0000381, 0.0000151, 0],
 [779, 0.0000357, 0.0000141, 0],
 [780, 0.0000334, 0.0000133, 0]])

Dxx1 = np.array([[380, 63.4, 38.5, 3],
 [385, 64.6, 36.75, 2.1],
 [390, 65.8, 35, 1.2],
 [395, 80.3, 39.2, 0.05],
 [400, 94.8, 43.4, -1.1],
 [405, 99.8, 44.85, -0.8],
 [410, 104.8, 46.3, -0.5],
 [415, 105.35, 45.1, -0.6],
 [420, 105.9, 43.9, -0.7],
 [425, 101.35, 40.5, -0.95],
 [430, 96.8, 37.1, -1.2],
 [435, 105.35, 36.9, -1.9],
 [440, 113.9, 36.7, -2.6],
 [445, 119.75, 36.3, -2.75],
 [450, 125.6, 35.9, -2.9],
 [455, 125.55, 34.25, -2.85],
 [460, 125.5, 32.6, -2.8],
 [465, 123.4, 30.25, -2.7],
 [470, 121.3, 27.9, -2.6],
 [475, 121.3, 26.1, -2.6],
 [480, 121.3, 24.3, -2.6],
 [485, 117.4, 22.2, -2.2],
 [490, 113.5, 20.1, -1.8],
 [495, 113.3, 18.15, -1.65],
 [500, 113.1, 16.2, -1.5],
 [505, 111.95, 14.7, -1.4],
 [510, 110.8, 13.2, -1.3],
 [515, 108.65, 10.9, -1.25],
 [520, 106.5, 8.6, -1.2],
 [525, 107.65, 7.35, -1.1],
 [530, 108.8, 6.1, -1],
 [535, 107.05, 5.15, -0.75],
 [540, 105.3, 4.2, -0.5],
 [545, 104.85, 3.05, -0.4],
 [550, 104.4, 1.9, -0.3],
 [555, 102.2, 0.95, -0.15],
 [560, 100, 0, 0],
 [565, 98, -0.8, 0.1],
 [570, 96, -1.6, 0.2],
 [575, 95.55, -2.55, 0.35],
 [580, 95.1, -3.5, 0.5],
 [585, 92.1, -3.5, 1.3],
 [590, 89.1, -3.5, 2.1],
 [595, 89.8, -4.65, 2.65],
 [600, 90.5, -5.8, 3.2],
 [605, 90.4, -6.5, 3.65],
 [610, 90.3, -7.2, 4.1],
 [615, 89.35, -7.9, 4.4],
 [620, 88.4, -8.6, 4.7],
 [625, 86.2, -9.05, 4.9],
 [630, 84, -9.5, 5.1],
 [635, 84.55, -10.2, 5.9],
 [640, 85.1, -10.9, 6.7],
 [645, 83.5, -10.8, 7],
 [650, 81.9, -10.7, 7.3],
 [655, 82.25, -11.35, 7.95],
 [660, 82.6, -12, 8.6],
 [665, 83.75, -13, 9.2],
 [670, 84.9, -14, 9.8],
 [675, 83.1, -13.8, 10],
 [680, 81.3, -13.6, 10.2],
 [685, 76.6, -12.8, 9.25],
 [690, 71.9, -12, 8.3],
 [695, 73.1, -12.65, 8.95],
 [700, 74.3, -13.3, 9.6],
 [705, 75.35, -13.1, 9.05],
 [710, 76.4, -12.9, 8.5],
 [715, 69.85, -11.75, 7.75],
 [720, 63.3, -10.6, 7],
 [725, 67.5, -11.1, 7.3],
 [730, 71.7, -11.6, 7.6],
 [735, 74.35, -11.9, 7.8],
 [740, 77, -12.2, 8],
 [745, 71.1, -11.2, 7.35],
 [750, 65.2, -10.2, 6.7],
 [755, 56.45, -9, 5.95],
 [760, 47.7, -7.8, 5.2],
 [765, 58.15, -9.5, 6.3],
 [770, 68.6, -11.2, 7.4],
 [775, 66.8, -10.8, 7.1],
 [780, 65, -10.4, 6.8]])


def Dxx(cct):
 if cct <= 7000 and cct >= 4000:
  Xd = -4.6070 * (10 ** 9) / (cct ** 3) + 2.9678 * (10 ** 6) / (cct ** 2) + (99.11 / cct) + 0.244063
 else:
  Xd = -2.0064 * (10 ** 9) / (cct ** 3) + 1.9018 * (10 ** 6) / (cct ** 2) + (247.48 / cct) + 0.23704
 Yd = -3 * (Xd ** 2) + 2.87 * Xd - 0.275
 M1 = (-1.3515 - 1.7703 * Xd + 5.9114 * Yd) / (0.0241 + 0.2562 * Xd - 0.7341 * Yd)
 M2 = (0.03 - 31.4424 * Xd + 30.0717 * Yd) / (0.0241 + 0.2562 * Xd - 0.7341 * Yd)
 s = Dxx1[:, 1] + M1 * Dxx1[:, 2] + M2 * Dxx1[:, 3]
 return s

# XYZ系统的标准观察者
def Field(Oq, xyz, d):
 if Oq == 2 :
  if xyz=='x':
   o=O2[:, 1]
  elif xyz=='y':
   o=O2[:, 2]
  else:o=O2[:, 3]
 elif Oq == 10:
  if xyz=='x':
   o=O2[:, 1]
  elif xyz=='y':
   o=O2[:, 2]
  else:o=O2[:, 3]
 else:
  print('输入有误')
  o=0
 dhg= []
 for aa in range(0,401,d):
  dhg.append(o[aa])
 return dhg


# print (Dxx1.shape[0])#统计行数
# print (Dxx1.shape[1])#统计列数
# print((Dxx1[Dxx1.shape[0]-1,0]-Dxx1[0,0])/5)

