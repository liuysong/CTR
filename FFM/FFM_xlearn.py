import xlearn as xl

# Training task
ffm_model = xl.create_ffm() # Use field-aware factorization machine
ffm_model.setTrain("./train_ffm.txt")  # Training data
ffm_model.setValidate("./test_ffm.txt")  # Validation data

# param:
#  0. binary classification
#  1. learning rate: 0.2
#  2. regular lambda: 0.002
#  3. evaluation metric: accuracy
param = {'task':'binary', 'lr': 0.2,
         'lambda':0.002, 'metric': 'acc',
         'opt': 'adagrad', 'k': 8, 'epoch':5}

ffm_model.cv(param)
# Start to train
# The trained model will be stored in model.out
ffm_model.fit(param, './model.out')

# Prediction task
ffm_model.setTest("./test_ffm.txt")  # Test data
ffm_model.setSigmoid()  # Convert output to 0-1

# Start to predict
# The output result will be stored in output.txt
ffm_model.predict("./model.out", "./output.txt")

