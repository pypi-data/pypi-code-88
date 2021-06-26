
class train_classifier():
  def __init__(self):
    model=FaceNet()
  
  def processed_data(train_data_path,validation_data_path):
    model=FaceNet()
    # Load the train images
    df_train = pd.read_csv('/d/project2/Input/train.csv')
    filenames_train=df_train[df_train.columns[0]]
    labels_train=df_train[df_train.columns[1]]

    embed_list_train=[]
    label_train_list=[]
    k=0
    for i in tqdm.tqdm(filenames_train):    
        faces_array_train = model.extract(i, threshold=0.95)
        for j in range(len(faces_array_train)):
            face_embed_dict=faces_array_train[j]
            face_embed=face_embed_dict['embedding']
            embed_list_train.append(face_embed)
            label_train_list.append(labels_train[k])
        k=k+1

    embed_list_train=np.array(embed_list_train)
    label_train_list=np.array(label_train_list)

    lb = LabelBinarizer()
    label_train_list = lb.fit_transform(label_train_list)
    label_train_list = to_categorical(label_train_list)

    df_val = pd.read_csv('/d/project2/Input/val.csv')
    filenames_val=df_val[df_val.columns[0]]
    labels_val=df_val[df_val.columns[1]]
    embed_list_val=[]
    label_val_list=[]
    k=0
    for i in tqdm.tqdm(filenames_val):    
        faces_array_val = model.extract(i, threshold=0.95)
        for j in range(len(faces_array_val)):
            face_embed_dict=faces_array_val[j]
            face_embed=face_embed_dict['embedding']
            embed_list_val.append(face_embed)
            label_val_list.append(labels_val[k])
        k=k+1

    embed_list_val=np.array(embed_list_val)
    label_val_list=np.array(label_val_list)

    lb = LabelBinarizer()
    label_val_list = lb.fit_transform(label_val_list)
    label_val_list = to_categorical(label_val_list)

    np.savez('svm_processed_data.npz', embed_list_train, label_train_list, embed_list_val, label_val_list)


  def svm_train(data_path):
    # load dataset
    data = load(data_path)
    trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
    # normalize input vectors
    in_encoder = Normalizer(norm='l2')
    trainX = in_encoder.transform(trainX)
    testX = in_encoder.transform(testX)
    # label encode targets
    trainy = np.argmax(trainy, axis=1)
    testy = np.argmax(testy, axis=1)
    # fit model
    model = SVC(kernel='linear', probability=True)
    model.fit(trainX, trainy)
    # predict
    yhat_train = model.predict(trainX)
    yhat_test = model.predict(testX)
    # score
    score_train = accuracy_score(trainy, yhat_train)
    score_test = accuracy_score(testy, yhat_test)
    # summarize
    print('Accuracy: train=%.3f, test=%.3f' % (score_train*100, score_test*100))

    # save the model to disk
    filename = 'svm_classifier_model_initial.sav'
    pickle.dump(model, open(filename, 'wb'))


