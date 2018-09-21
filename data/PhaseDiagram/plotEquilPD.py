import numpy as np
import math
import matplotlib.pyplot as plt


n = np.array([-3.99998775e+00, -3.91998774e+00, -3.83998772e+00, -3.75998774e+00,
          -3.67998775e+00, -3.59998771e+00, -3.51998773e+00, -3.43998772e+00,
          -3.35998771e+00, -3.27998773e+00, -3.19998774e+00, -3.11998772e+00,
          -3.03998775e+00, -2.95998772e+00, -2.87998774e+00, -2.79998773e+00,
          -2.71998775e+00, -2.63998772e+00, -2.55998773e+00, -2.47998774e+00,
          -2.39998773e+00, -2.31998773e+00, -2.23998773e+00, -2.15998774e+00,
          -2.07998772e+00, -1.99998773e+00, -1.91998771e+00, -1.83998773e+00,
          -1.75998772e+00, -1.67998774e+00, -1.59998775e+00, -1.51998774e+00,
          -1.43998773e+00, -1.35998772e+00, -1.27998772e+00, -1.19998771e+00,
          -1.11998774e+00, -1.03998774e+00, -9.59987712e-01, -8.79987746e-01,
          -7.99987727e-01, -7.19987724e-01, -6.39987731e-01, -5.59987715e-01,
          -4.79987742e-01, -3.99987706e-01, -3.19987735e-01, -2.39987716e-01,
          -1.59987729e-01, -7.99877396e-02,  1.22564527e-05,  8.00122873e-02,
           1.60012266e-01,  2.40012282e-01,  3.20012264e-01,  4.00012278e-01,
           4.80012272e-01,  5.60012262e-01,  6.40012281e-01,  7.20012259e-01,
           8.00012267e-01,  8.80012266e-01,  9.60012291e-01,  1.04001228e+00,
           1.12001227e+00,  1.20001227e+00,  1.28001227e+00,  1.36001226e+00,
           1.44001228e+00,  1.52001229e+00,  1.60001227e+00,  1.68001227e+00,
           1.76001226e+00,  1.84001227e+00,  1.92001226e+00,  2.00001228e+00,
           2.08001229e+00,  2.16001227e+00,  2.24001228e+00,  2.32001229e+00,
           2.40001227e+00,  2.48001228e+00,  2.56001227e+00,  2.64001229e+00,
           2.72001226e+00,  2.80001226e+00,  2.88001228e+00,  2.96001228e+00,
           3.04001228e+00,  3.12001229e+00,  3.20001226e+00,  3.28001226e+00,
           3.36001227e+00,  3.44001227e+00,  3.52001229e+00,  3.60001228e+00,
           3.68001226e+00,  3.76001227e+00,  3.84001228e+00,  3.92001228e+00])

T_0 = np.array([4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958,
         4.00000958, 4.00000958, 4.00000958, 4.00000958, 4.00000958])

T_500 = np.array([ 3.93533169,  3.93131035,  3.92729658,  3.92327517,  3.91923106,
           3.91515625,  3.91104023,  3.90687149,  3.90263854,  3.89834055,
           3.89394826,  3.88930276,  3.88434141,  3.87901154,  3.87323816,
           3.86693032,  3.85998044,  3.85225885,  3.84358984,  3.83349984,
           3.82156098,  3.80733532,  3.7902477 ,  3.76938762,  3.74362932,
           3.71150169,  3.6709477 ,  3.61949968,  3.5534473 ,  3.46698   ,
           3.35076419,  3.1896263 ,  2.95665939,  2.61711162,  2.18638271,
           1.71545501,  1.18128118,  0.85927273,  0.6796425 ,  0.55049292,
           0.44558131,  0.35473277,  0.27304987,  0.19820452,  0.12777108,
           0.06063033, -0.0039566 , -0.06658909, -0.10022212, -0.100056  ,
          -0.10008122, -0.10027418, -0.10057621, -0.10036913, -0.10107149,
          -0.10121065, -0.1012507 , -0.10139987, -0.10173935, -0.10172366,
          -0.10027755, -0.10374872, -0.10121581, -0.10484279, -0.10474645,
          -0.10015531, -0.10429365, -0.11170594, -0.1083502 , -0.11122161,
          -0.10170901, -0.10229305, -0.12582257, -0.10272125, -0.11063037,
          -0.10913129, -0.13942258, -0.14126785, -0.09999863, -0.14473121,
          -0.10455797, -0.10861281, -0.13324813, -0.13679977, -0.12642739,
          -0.11469017, -0.10044367, -0.13214331, -0.11816457, -0.11816457,
          -0.11816457, -0.11816457, -0.11816457, -0.11816457, -0.11816457,
          -0.11816457, -0.11816457, -0.11816457, -0.11816457, -0.11816457])

T_1000 = np.array([ 3.92020737,  3.91614085,  3.91203573,  3.90788032,  3.90366395,
          3.89937973,  3.89502089,  3.89044281,  3.88556191,  3.88032553,
          3.87466597,  3.86849745,  3.86172078,  3.85420401,  3.84579653,
          3.83610062,  3.82464125,  3.81101006,  3.79466527,  3.77480409,
          3.75033602,  3.7199183 ,  3.68163784,  3.63308817,  3.5709066 ,
          3.49009784,  3.38236339,  3.23440198,  3.02360075,  2.71390592,
          2.29370483,  1.83944559,  1.29675748,  0.91839443,  0.71725404,
          0.57948888,  0.47001167,  0.37641507,  0.29284802,  0.21608869,
          0.14455473,  0.07672414,  0.01156338, -0.05153234, -0.0999221 ,
         -0.10021245, -0.10007505, -0.1001572 , -0.10001389, -0.10058247,
         -0.10078468, -0.10074332, -0.1002994 , -0.10005843, -0.10100561,
         -0.10148297, -0.10086705, -0.10115432, -0.10113556, -0.10332398,
         -0.10568004, -0.10332129, -0.10444852, -0.10385485, -0.10283917,
         -0.10284679, -0.10882396, -0.10406178, -0.1121769 , -0.10896278,
         -0.13207839, -0.14370687, -0.14230666, -0.12724547, -0.13445192,
         -0.10240875, -0.11324881, -0.12197308, -0.12552283, -0.10867222,
         -0.11712911, -0.12297055, -0.12784251, -0.11816457, -0.11816457,
         -0.11816457, -0.11816457, -0.11816457, -0.11816457, -0.11816457,
         -0.11816457, -0.11816457, -0.11816457, -0.11816457, -0.11816457,
         -0.11816457, -0.11816457, -0.11816457, -0.11816457, -0.11816457])

T_1500 = np.array([ 3.91124411e+00,  3.90707767e+00,  3.90284848e+00,  3.89855221e+00,
          3.89416651e+00,  3.88953505e+00,  3.88459016e+00,  3.87927718e+00,
          3.87352637e+00,  3.86725304e+00,  3.86034568e+00,  3.85267212e+00,
          3.84406509e+00,  3.83406842e+00,  3.82223861e+00,  3.80813749e+00,
          3.79120774e+00,  3.77056517e+00,  3.74509575e+00,  3.71334462e+00,
          3.67334956e+00,  3.62258904e+00,  3.55743003e+00,  3.47229547e+00,
          3.35822723e+00,  3.20086084e+00,  2.97526679e+00,  2.64621531e+00,
          2.21844244e+00,  1.75278957e+00,  1.21343692e+00,  8.75670760e-01,
          6.90122308e-01,  5.58602139e-01,  4.52794095e-01,  3.61497188e-01,
          2.79525775e-01,  2.03961433e-01,  1.32997644e-01,  6.54511085e-02,
          4.95357082e-04, -6.24589368e-02, -9.99437694e-02, -1.00037288e-01,
         -9.99927470e-02, -9.99400686e-02, -1.00167030e-01, -1.00008416e-01,
         -1.00222123e-01, -1.00056003e-01, -1.00081217e-01, -1.00274177e-01,
         -1.00576215e-01, -1.00369125e-01, -1.01071489e-01, -1.01210655e-01,
         -1.01250701e-01, -1.01399868e-01, -1.01739355e-01, -1.01723664e-01,
         -1.00277552e-01, -1.03748722e-01, -1.01215810e-01, -1.04842792e-01,
         -1.04746445e-01, -1.00155305e-01, -1.04293647e-01, -1.11705942e-01,
         -1.08350204e-01, -1.11221608e-01, -1.01709007e-01, -1.02293050e-01,
         -1.25822569e-01, -1.02721252e-01, -1.10630373e-01, -1.09131289e-01,
         -1.39422583e-01, -1.41267846e-01, -9.99986280e-02, -1.44731209e-01,
         -1.04557971e-01, -1.08612815e-01, -1.33248127e-01, -1.36799771e-01,
         -1.26427393e-01, -1.14690168e-01, -1.00443674e-01, -1.32143307e-01,
         -1.18164568e-01, -1.18164568e-01, -1.18164568e-01, -1.18164568e-01,
         -1.18164568e-01, -1.18164568e-01, -1.18164568e-01, -1.18164568e-01,
         -1.18164568e-01, -1.18164568e-01, -1.18164568e-01, -1.18164568e-01])

def plotEquilPD(snap):

    if(snap == '0000'):
        plt.plot(n, T_0, '--', c='red')
    if(snap == '0500'):
        plt.plot(n, T_500, '--', c='red')
    if(snap == '1000'):
        plt.plot(n, T_1000, '--', c='red')
    if(snap == '1500'):
        plt.plot(n, T_1500, '--', c='red')
        
if __name__ == '__main__':
    plotEquilPD('0500')

