

def load_labels(label_file):
    label = {}
    count = 0
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label[l.strip()] = count
        count += 1
    return label

x_test,y_test=load_data("/Users/anna/SLR/Seperate/testinput/")
new_model = tf.keras.models.load_model('simpeRNN.h5')
new_model.summary()

#모델평가
#loss, acc = new_model.evaluate(x_test,y_test, verbose=2)
#print('Restored model, accuracy: {:5.2f}%'.format(100*acc))

#print(new_model.predict(x_test).shape)


#모델 사용

xhat = x_test
yhat = new_model.predict(xhat)
print('## yhat ##')
#labels=load_label(dirname) 
a=xhat.shape[0]
for i in range(a):
    print('True: '+str(argmax(y_test[i]))+', Predict: '+str(yhat[i]))
    
