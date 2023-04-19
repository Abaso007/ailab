"""
Configuration for the generate module
"""


#-----------------------------------------------------------------------------#
# Flags for running on CPU
#-----------------------------------------------------------------------------#
FLAG_CPU_MODE = False

paths = {
    'skmodels': '../models/skvmodel_adventure.npz',
    'sktables': '../models/',
    'decmodel': '../models/decmodel.npz',
    'dictionary': '../models/dict.pkl',
    'vsemodel': '../models/coco_embedding.npz',
    'vgg': '../models/vgg_weights.npy',
    'pycaffe': 'models/python',
    'vgg_proto_caffe': 'models/VGG_ILSVRC_19_layers_deploy.prototxt',
    'vgg_model_caffe': 'models/VGG_ILSVRC_19_layers.caffemodel',
    'captions': '../models/coco_train_caps.txt',
    'negbias': '../models/caption_style.npy',
    'posbias': '../models/adventure_style.npy',
    'text': '../models/text.pkl',
    'v_expansion': '../models/GoogleNews-vectors-negative300.bin',
    'books': '../books/adventure/*.txt',
}
settings = {
    'decoder': {
        'dimctx': 4800,
        'dim_word': 620,
        'dim': 2400,
        'encoder': 'gru',
        'decoder': 'gru',
        'doutput': False,
        'max_epochs': 1,
        'disp_freq': 1,
        'decay_c': 0.0,
        'grad_clip': 5.0,
        'n_words': 20000,
        'maxlen_w': 200,
        'optimizer': 'adam',
        'batch_size': 1,
        'saveto': paths['decmodel'],
        'dictionary': paths['dictionary'],
        'embeddings': None,
        'save_freq': 200,
        'sample_freq': 20,
        'reload_': True,
    },
    'encoder': {
        'dim_word': 620,
        'dim': 4800,
        'encoder': 'gru',
        'decoder': 'gru',
        'max_epochs': 1,
        'disp_freq': 1,
        'decay_c': 0.0,
        'grad_clip': 5.0,
        'n_words': 20000,
        'maxlen_w': 30,
        'optimizer': 'adam',
        'batch_size': 1,
        'saveto': paths['skmodels'],
        'dictionary': paths['dictionary'],
        'save_freq': 200,
        'reload_': True,
    },
}
