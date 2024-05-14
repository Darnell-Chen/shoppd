import firebase_admin
from firebase_admin import credentials, storage, firestore
import torch
import pickle
import time
import instantiate_firebase

# firebase storage is wrapper for gcs - view documentation here: 
# https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob#google_cloud_storage_blob_Blob_upload_from_file
def storeTo(path, info: dict):
    # converts the dict into an object file in memory
    pickled_vectors = pickle.dumps(info)

    bucket = storage.bucket()
    blob = bucket.blob("scraped_items/" + path)

    # the current file will automatically be overwritten :)
    blob.upload_from_string(pickled_vectors)

    # function that sets the time of when the last webscrape occured (i.e. current time)
    markTime(path)


def getVectors(path):

    bucket = storage.bucket()
    blob = bucket.blob("scraped_items/" + path)
    pickled_info = blob.download_as_bytes()

    finalInfo = pickle.loads(pickled_info)

    return finalInfo


def markTime(path):
    currTime = time.time()

    db = firestore.client()
    doc_ref = db.collection("web_scraping").document(path)
    doc_ref.set({"time" : str(currTime)})


def getTime(path):

    db = firestore.client()
    doc_ref = db.collection("web_scraping").document(path)
    timeRef = doc_ref.get()._data
    return float(timeRef.get("time"))



if __name__ == "__main__":

    testInfo = {'Screenshot 2024-02-10 at 9.33.52\u202fPM.png': torch.tensor([[ 9.7868e-03,  1.0841e-01,  7.3568e-03,  3.6547e-01, -3.5428e-01,
          6.4919e-01, -7.6568e-01,  3.9171e-01,  8.1750e-01,  1.6854e-01,
         -1.2365e-01,  2.0357e-01, -9.7830e-02, -1.2372e-01, -3.2671e-01,
         -2.5588e-02, -8.3539e-02,  2.8845e-01,  8.5146e-02,  2.0050e-02,
         -2.8506e-01, -3.9998e-01,  2.9018e-01, -6.2507e-01, -4.0486e-02,
          8.0910e-02,  2.3737e-01, -7.1669e-02,  2.7473e-01, -4.3657e-01,
         -2.7810e-02,  2.3381e-01, -2.0335e-01,  4.7001e-02,  2.1185e-01,
         -1.5332e-01, -4.8321e-02,  3.1312e-01, -2.3872e-01,  1.5241e+00,
         -6.4360e-01, -2.0938e-01, -2.8412e-02, -1.1499e-01,  1.5712e-01,
         -5.7763e-01, -1.9273e-01,  2.3027e-01,  2.0327e-01,  9.6631e-02,
          3.6472e-01,  2.1582e-01,  1.2440e-01,  1.7432e-01, -3.2703e-01,
          3.1882e-01,  3.9163e-01, -6.9183e-02,  5.9355e-03,  4.5870e-01,
          5.1622e-01,  9.5062e-02,  2.7912e-01,  2.7485e-01, -1.9518e-01,
         -2.1539e-01, -2.5039e-01, -4.7015e-01, -9.2077e-03,  1.0393e-01,
         -1.8951e-01, -3.0651e-01, -3.4171e-01,  3.2218e-01,  2.0817e-01,
         -2.4686e-01,  3.6689e-01, -1.7923e-02, -3.7495e-01,  4.6556e-01,
         -3.0429e-01, -1.2316e-01, -3.8985e-01,  4.9428e-01,  3.9557e-02,
          2.2204e-01,  4.3299e-01, -5.3222e-01, -1.5149e-01, -9.2617e-02,
          3.1605e-01,  4.0111e-01, -6.4830e+00,  8.5964e-01, -4.3914e-01,
          1.6640e-01, -6.9890e-02, -8.2830e-02, -6.7629e-01,  1.0762e+00,
         -3.2177e-01, -5.6940e-01,  3.1777e-01,  5.1563e-02, -1.6079e-01,
          4.4056e-01,  3.6136e-01, -1.7399e-01,  9.7081e-02,  4.9749e-01,
         -6.7702e-02,  7.3941e-01, -3.7131e-01, -1.7110e-01, -1.1195e-01,
          1.4640e-01, -7.2404e-01, -1.2186e-01,  2.6111e-01,  5.6730e-01,
          2.4226e-01, -1.1898e-03,  2.4621e-01, -2.2334e-01, -1.1524e-01,
         -6.3191e-01, -1.9718e-01,  1.5548e-01,  6.9533e-02,  2.5665e-01,
          2.8018e-01,  1.5896e-01,  8.1342e-02,  8.0277e-01,  4.0589e-01,
          3.0127e-01, -2.2175e-01,  1.5449e-01,  1.0785e-01,  7.2614e-02,
          2.0202e-03,  3.4339e-02, -1.3342e-01,  3.0142e-01, -3.3709e-01,
          4.3096e-01,  1.7770e-01,  4.0311e-01, -1.5232e-01, -2.2236e-02,
          9.4429e-02, -2.8210e-01,  9.8160e-01, -1.8626e-01,  6.4193e-04,
         -2.3586e-01,  5.0993e-01, -2.2454e-01,  1.7825e-01,  2.5329e-01,
          1.5236e-01,  1.9072e-01,  3.6505e-01, -4.3510e-02,  2.8840e-01,
          3.4250e-01,  1.3660e-01, -1.7407e-01, -1.2810e-01,  1.1102e-01,
         -2.1938e-01, -2.6164e-01,  4.5338e-01,  3.2310e-01,  1.0586e-01,
          1.0362e-01,  6.9026e-01, -1.8339e-01,  3.7564e-01, -3.5730e-01,
          8.4259e-01,  1.2664e-01,  4.5388e-01,  1.8590e-01, -4.4704e-02,
          4.0544e-01,  1.2136e-01, -2.2681e-01, -1.0529e-01, -5.7099e-02,
          5.5447e-01,  3.0952e-01, -2.4385e-02,  2.1992e-01,  3.0034e-01,
         -2.4442e-01,  1.0512e-01, -9.6198e-02,  3.3697e-01,  1.5027e-01,
         -7.7005e-02, -3.1998e-01,  2.8413e-01,  3.5460e-03, -5.4866e-02,
         -3.6514e-01, -5.7907e-01,  7.0827e-03, -1.2943e-01,  1.7415e-01,
          1.1567e-01,  4.9697e-01,  2.2322e-03, -4.7068e-02, -4.7935e-01,
         -7.6896e-02,  5.7314e-02,  4.9560e-01,  1.7623e-01,  2.5422e-01,
         -1.5262e-01, -1.0160e+00,  1.5700e-01,  3.7346e-01, -4.5942e-01,
         -1.4446e-01,  1.8794e-01, -3.0968e-01,  2.2483e-01,  4.2344e-01,
         -1.0043e-01, -1.1877e-01, -1.8009e-02,  1.2772e-01,  1.4361e-02,
         -8.2564e-01,  8.4286e-02,  8.1337e-02, -2.3269e-01,  1.4983e-01,
          1.7350e-01,  5.3591e-01,  1.3259e-01, -6.1442e-01, -2.7905e-01,
         -4.7164e-01, -3.3301e-01,  6.3538e-01,  2.0606e-01, -3.5917e-01,
          2.3226e-01, -2.6323e-01, -3.8430e-02, -1.2010e-01, -1.5311e-01,
          4.8666e-01, -3.0043e-01,  1.3871e-01, -1.3522e+00,  1.7044e-01,
          4.5130e-01, -4.2691e-01, -2.5483e-01, -1.5275e-01, -1.8153e-01,
         -3.7054e-02, -1.0241e-01,  1.0473e-01,  4.2809e-02, -1.3821e-01,
         -3.1197e-01,  5.0486e-01,  7.0271e-02, -7.0620e-01,  2.8622e-01,
          1.6491e-01, -1.9561e-01,  4.6155e-01, -2.0038e-01,  4.1038e-02,
         -2.3351e-01, -7.2669e-03, -3.4529e-01, -1.0072e-02, -4.6450e-02,
         -3.6022e-01,  9.7361e-01, -1.0664e-01,  1.6894e-01, -5.9145e-02,
          4.5495e-03, -1.0666e-02,  3.4308e-01,  6.3685e-02, -2.1927e-01,
          3.3745e-01, -1.5221e-01,  5.9504e-02,  8.1103e-01,  5.4146e-01,
         -1.2052e-01, -1.7905e-01,  2.1844e-01, -2.7540e-01,  6.0654e-01,
         -1.6318e-01,  5.9676e-02,  5.4085e-01, -2.7857e-02, -6.2940e-03,
         -3.3424e-01,  4.8882e-01,  8.0244e-01,  3.5997e-01,  5.1155e-02,
         -1.1480e-01,  4.7458e-01, -1.6564e-01,  5.2335e-01,  5.7154e-01,
         -2.3263e-01,  1.7044e+00, -1.5046e-01, -4.6005e-01,  2.4370e-01,
         -1.8139e-01,  8.8205e-02,  3.0925e-01,  2.0623e-01, -2.2105e-01,
         -1.8767e-01, -1.3804e-01, -4.8369e-01,  5.2413e-02, -3.6429e-02,
         -2.1928e-01,  5.7113e-01, -1.2481e-01,  2.3443e-01,  6.0123e-01,
         -4.3177e-01, -6.4818e-02, -7.6884e-02,  6.2213e-01, -5.7106e-02,
          2.4201e-01, -5.3782e-03, -1.4793e-01, -3.6213e-01, -1.5252e-01,
          9.5747e-01, -1.3953e-01, -1.4336e-01, -1.8686e-01,  2.5614e-02,
         -2.7428e-01, -2.5822e-01,  8.1054e-01,  2.6650e-01, -5.8269e-02,
          1.6225e+00, -4.0128e-01, -2.1377e-01, -3.7676e-01,  7.0047e-01,
         -1.4953e-01, -3.5513e-01, -8.4248e-01, -7.9696e-02,  4.3567e-01,
          3.2197e-01,  2.2168e-01,  4.1623e-01,  2.6189e-01,  2.1318e-02,
         -4.1216e-01,  9.0756e-01,  4.0772e-02, -1.8783e-01,  2.5694e-01,
         -1.1192e-01, -2.2451e-01, -5.8318e-01, -7.4775e-01, -9.2955e-02,
          2.1282e-01,  1.1139e-01,  1.4929e-01, -3.3024e-01, -2.4276e-02,
         -1.1850e+00,  9.3904e-02,  1.0283e-01,  9.8455e-02, -4.4062e-01,
         -3.5172e-01,  1.8193e-01, -3.0214e-01,  2.0333e-01,  1.4631e-01,
          1.9713e-01,  2.3508e-01,  1.3419e+00, -5.2014e-01,  2.7200e-01,
          3.2340e-01, -1.2122e-01,  2.1077e-02,  4.5669e-01, -1.6840e-01,
         -6.1512e-02,  1.3159e-01, -4.4665e-01, -2.6094e-01, -6.9977e-01,
          3.2386e-02,  4.9174e-01,  5.1415e-01, -5.0124e-01, -5.3803e-01,
          4.6928e-01,  2.1293e-01,  7.0887e-01,  2.6509e-01,  6.7876e-02,
          2.7960e-02, -1.5390e-01, -1.1510e-01, -3.1516e+00, -4.6968e-02,
         -3.8388e-02,  1.4020e-01,  1.0329e+00, -1.2079e-01, -1.7283e-01,
         -1.2118e-01, -1.3479e-01,  3.2918e-01,  6.7296e-01,  2.2735e-01,
          2.0786e-01,  4.1452e-01,  3.4502e-01, -6.9649e-02,  5.0471e-01,
         -2.5841e-01,  2.7538e-02, -7.1375e-02, -3.8594e-01, -3.7431e-02,
          1.4260e-01,  2.5695e-01,  5.5186e-01,  2.2249e-02, -4.4306e-01,
          4.7478e-01, -3.5715e-01, -7.4134e-03,  8.1492e-02,  4.2839e-01,
          2.1074e-01, -3.0680e-01, -1.7520e-01, -1.4264e-01,  2.7297e-01,
         -2.3172e-01,  1.4197e-01, -5.0139e-02, -1.9918e-01,  1.9872e-01,
         -1.6872e-01, -1.8710e-01,  4.6484e-01, -5.5511e-01,  2.8195e-01,
          1.3337e-01, -1.8091e-01,  4.0378e-01,  5.8378e-01, -1.0505e-01,
          9.0307e-02, -1.5424e-01, -1.9108e-01,  7.8133e-02,  4.2786e-02,
          7.2475e-02, -1.1722e-01, -1.7047e-01, -1.5901e-01, -7.3923e-01,
          3.9674e-01, -1.3631e-01,  4.6705e-02,  3.0955e-01, -5.0331e-03,
         -4.9929e-01,  3.4248e-01,  1.9826e-01,  7.9948e-02,  8.8032e-02,
         -3.3713e-01, -5.1026e-02, -3.7690e-01, -3.8812e-03,  1.3286e-01,
          1.4540e-01, -3.0753e-01, -4.8757e-02,  1.1389e-01,  2.5032e-01,
         -2.5375e-01,  1.3269e-01]]), 'Screenshot 2024-02-10 at 9.33.58\u202fPM.png': torch.tensor([[ 1.7036e-01, -3.2939e-03,  1.9068e-01,  1.8205e-01,  5.2411e-02,
          2.9988e-01,  1.3044e-01,  2.7498e-01,  1.1478e+00,  2.2015e-01,
         -1.6969e-01,  4.4178e-01,  2.5230e-01,  3.1263e-01, -1.0925e-01,
         -1.0865e-01,  8.1211e-02,  9.4150e-02, -1.2186e-02, -2.6366e-02,
         -5.6607e-01, -2.0733e-01,  1.5237e-01, -1.9059e-01, -1.7104e-01,
          2.9130e-01, -4.0533e-01, -4.2377e-01,  1.2765e-01, -3.1144e-01,
         -1.8465e-02,  8.8580e-02,  9.6128e-02,  1.0682e-01, -8.0337e-02,
          1.5798e-02, -1.6029e-01,  6.5259e-01, -2.8732e-01,  1.2849e+00,
         -6.7486e-01, -2.4554e-01, -6.1145e-02,  1.0285e-01,  1.3197e-01,
         -1.2028e+00, -2.2549e-01,  3.1188e-01,  3.9913e-01,  2.0359e-01,
          6.4813e-01, -9.1574e-03,  8.0272e-02, -1.1661e-01, -4.4352e-01,
          5.5509e-01,  3.4866e-01,  2.2765e-01,  2.5274e-01,  5.3393e-01,
          3.3713e-01, -4.0027e-01,  1.8418e-01, -2.4682e-01, -2.4733e-01,
          1.0151e-02,  9.7235e-02, -9.6675e-01, -8.0491e-02,  3.2072e-01,
         -3.6825e-01, -1.8691e-02, -1.0356e-01, -2.0330e-01, -2.3907e-01,
          2.9551e-01,  2.6180e-01,  1.5710e-01,  1.5320e-01,  3.9935e-01,
         -1.8168e-01, -4.7900e-01, -4.2327e-02,  4.3825e-01,  1.8090e-01,
          2.2424e-01,  4.9567e-01, -4.7286e-01, -4.3244e-01, -2.1813e-01,
          3.6093e-01,  1.4858e-01, -7.4222e+00,  5.7426e-01, -1.1798e-01,
          4.8558e-01, -3.6226e-01, -3.3214e-01,  2.8035e-01,  1.4667e+00,
         -1.5069e-01, -5.0715e-02,  1.8709e-01, -8.0216e-02, -1.0895e-01,
          1.5137e-01, -5.0710e-02,  1.3787e-01, -4.3273e-01,  3.3134e-01,
         -1.9984e-01,  9.2326e-02, -8.0388e-03, -2.6412e-01, -9.9598e-02,
          3.8895e-03, -4.8135e-01,  6.1983e-02, -7.9752e-02,  1.7375e-01,
          5.3491e-01, -6.5651e-02, -2.3216e-01,  5.4807e-02, -2.9242e-01,
          3.6811e-01, -1.9698e-01,  6.1125e-02,  2.5771e-01,  7.3285e-02,
         -1.2062e-02,  8.6033e-02,  5.7198e-02,  9.1571e-01,  1.0273e-01,
          2.4918e-01, -9.0084e-02,  1.3060e-01, -2.1885e-01, -2.9887e-02,
         -5.8805e-02, -9.9119e-02, -5.4377e-01,  4.4738e-02, -4.1315e-01,
         -4.0516e-01, -2.1316e-01,  5.0191e-01, -2.7094e-01, -1.2649e-01,
         -8.3883e-02, -4.9783e-01,  1.2074e+00,  4.3754e-01, -1.5916e-01,
         -1.6937e-02,  3.6465e-01,  2.5818e-01, -5.5276e-02,  2.5888e-01,
         -4.2996e-02,  8.1836e-02,  5.5096e-01, -3.6929e-01, -1.1111e-01,
         -2.4940e-01,  7.5050e-04,  1.1725e-01, -2.0057e-01,  1.1742e-01,
         -7.7590e-02,  1.4754e-01,  1.8429e-02, -8.7011e-03, -4.7069e-01,
         -4.1249e-02,  8.9182e-01,  1.1361e-01,  7.3927e-01, -5.7871e-02,
          9.0213e-01, -8.4928e-02,  7.9153e-01, -3.0826e-01, -4.8266e-01,
         -6.2626e-02,  1.4880e-01, -2.2931e-01, -1.6017e-01,  8.2744e-02,
         -7.0952e-02, -3.6424e-02,  1.8104e-02, -1.8625e-01,  1.3037e-01,
         -1.5236e-01,  1.2776e-01, -5.8048e-02, -1.9268e-01, -3.1376e-02,
         -2.7569e-01, -1.7200e-01, -1.1874e-01, -7.7823e-02,  2.8923e-01,
         -1.0128e-01, -3.4963e-01, -2.7928e-01,  3.4890e-01,  1.5408e-01,
         -2.4809e-01,  8.8715e-01,  4.5415e-02, -2.4185e-01, -3.4742e-01,
         -5.4672e-01,  1.6769e-01,  4.6667e-01,  1.3984e-01, -8.6099e-02,
         -4.5611e-01, -6.6734e-01, -2.8079e-01,  3.5522e-01,  4.4563e-02,
          1.8919e-01,  2.7422e-01, -5.6404e-02,  6.3558e-02,  3.1520e-01,
          1.2317e-01, -2.3191e-01,  1.4539e-01, -5.9661e-03,  5.4763e-02,
         -2.7864e-01,  1.1459e-01, -2.0303e-01,  8.3161e-02,  3.4182e-01,
         -1.3743e-01,  2.1915e-01,  3.7917e-01, -5.7342e-01, -1.3596e-01,
         -3.6592e-01,  1.6299e-01,  4.7220e-01, -9.9258e-03, -2.3137e-01,
          3.3598e-01, -4.0584e-02,  3.5815e-01, -2.8640e-01, -1.4212e-01,
          4.3384e-01,  4.3876e-02,  2.2430e-01, -1.6145e+00,  1.6863e-02,
          2.4269e-01,  2.1906e-02, -4.9277e-01,  1.7305e-01, -2.6681e-01,
         -2.4902e-01, -3.8439e-02, -9.1953e-02,  1.3184e-01, -1.8062e-01,
          1.6916e-01,  4.8234e-01,  4.9973e-02, -1.9896e-01,  3.0565e-01,
          1.0472e-01, -3.9933e-01,  3.0756e-01, -4.0427e-01, -1.1141e-01,
         -3.7918e-01, -3.8158e-02, -7.4882e-01, -5.2133e-01, -3.3406e-01,
         -6.1571e-02, -1.1941e-01, -2.2062e-01, -5.0375e-02,  4.3580e-01,
          5.8833e-01, -1.6517e-01,  1.5931e-02, -5.4570e-02, -3.3181e-01,
          1.4347e-01, -4.8026e-01,  2.0754e-01,  4.4320e-02,  2.8888e-02,
         -3.2671e-02, -3.4087e-01, -2.1844e-01, -3.8877e-01,  6.9564e-03,
         -7.4590e-01, -1.9881e-01,  3.2827e-01,  1.6847e-01, -1.3821e-01,
         -2.3880e-01,  1.8299e-01,  9.1623e-01,  1.5137e-01,  4.6473e-01,
          9.5150e-02,  3.2395e-01, -1.9972e-01,  6.8641e-02, -2.5701e-01,
          6.5510e-02,  2.1174e+00, -4.9338e-01, -7.1194e-01,  2.5862e-01,
         -8.5175e-02,  1.7283e-01,  1.1512e-01, -1.0690e-01,  1.1720e-01,
         -5.1079e-02, -2.1050e-01, -3.9741e-01, -9.5223e-02,  3.5805e-02,
          6.0127e-01,  7.9933e-02, -1.9384e-01, -2.7415e-01,  1.1759e-01,
         -1.6076e-01, -3.6330e-01,  1.2464e-01,  4.6106e-01,  7.5599e-03,
          1.6592e-01,  1.1755e-02, -3.6089e-01,  4.8511e-02, -1.8651e-01,
          6.8786e-01,  2.4450e-01, -6.4204e-02, -1.1531e-01,  8.1146e-02,
         -5.7357e-01, -5.0854e-01,  4.7141e-01, -3.2182e-01, -7.7097e-01,
          1.1991e+00, -1.2530e-01, -2.2137e-01, -1.7976e-01, -5.4762e-01,
         -3.9167e-01, -2.0841e-01, -7.1664e-01, -1.4806e-01, -6.9644e-02,
          1.5850e-01, -1.9930e-01,  2.8984e-01, -6.9663e-05,  2.1863e-01,
         -3.9678e-01,  7.0195e-01, -4.1611e-02, -6.2556e-01, -1.0084e-01,
         -8.1901e-02, -4.7733e-02, -2.8901e-01, -1.1497e-01, -4.0960e-01,
          6.7965e-02, -1.5423e-01,  6.9231e-03, -3.0876e-01,  5.7494e-01,
         -8.8849e-01, -8.8896e-02, -8.8641e-02,  2.1315e-01, -5.5206e-02,
          1.3218e-01,  6.0384e-02, -6.8833e-02, -1.0300e-01,  1.5183e-01,
          2.7037e-01,  1.1200e-01,  1.3431e+00, -4.3231e-01,  1.5873e-01,
         -2.8680e-01, -2.7191e-01, -1.4372e-01,  5.3991e-01, -2.9976e-01,
         -3.2418e-02, -3.7172e-01,  1.4649e-01, -3.0548e-03, -5.5849e-01,
         -1.2223e-01,  1.7421e-01,  7.9844e-01, -3.5892e-01, -6.6578e-01,
          1.7613e-01, -8.4669e-02,  4.9962e-01,  5.3712e-01,  2.2665e-02,
         -8.6249e-03,  1.5143e-01,  1.4538e-01, -1.7910e+00,  2.3377e-01,
         -1.4833e-01, -2.5456e-02,  1.3835e+00,  8.7924e-02, -1.0312e-01,
          4.3682e-02,  2.4672e-01,  4.7904e-02,  7.3331e-01,  1.6474e-01,
         -8.6619e-02,  4.5786e-01, -9.3302e-02,  3.0560e-01, -1.3202e-01,
         -2.4390e-01,  1.2481e-01,  5.0649e-02, -5.6347e-01, -6.7051e-02,
          9.9282e-02,  8.5553e-02,  3.8464e-01, -2.2821e-01, -1.2360e-01,
          6.0365e-01, -2.6295e-01,  1.9229e-01, -1.7189e-01, -1.4716e-01,
          2.7248e-02,  1.3182e-01, -6.7983e-01, -1.7278e-01,  2.0782e-01,
          2.9221e-01,  5.3134e-01,  9.3403e-03,  8.6033e-02,  4.1215e-02,
          2.0177e-01, -3.8683e-02,  3.8265e-01, -7.7738e-02, -2.7507e-01,
         -2.3880e-01,  1.7914e-01, -8.5148e-02,  3.2727e-02, -5.5011e-02,
         -1.7154e-01, -2.4266e-01, -1.8932e-01,  1.9383e-01,  3.4134e-01,
         -9.9790e-02,  3.8821e-02,  2.3324e-01, -2.6014e-01, -2.4852e-01,
          1.7763e-01, -3.6862e-02,  1.7733e-01, -2.4169e-01, -2.4127e-01,
         -5.8345e-01,  3.0521e-01,  1.4837e-01,  1.5219e-02,  3.0581e-01,
         -2.6280e-01,  1.5377e-02, -3.4061e-01, -5.0707e-01,  5.4492e-01,
         -9.5844e-02, -2.3262e-01,  3.0264e-01, -2.4265e-01,  6.2557e-01,
          5.0203e-03,  1.3433e-01]])}
    
    # storeTo("testStoring", testInfo)
    # getVectors("testStoring")
    getTime("testStoring")