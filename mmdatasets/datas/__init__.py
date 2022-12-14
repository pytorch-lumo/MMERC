from functools import partial

from lumo import Logger

if __name__ == '__main__':
    from mm import iemocap_raw, iemocap_feature, meld_feature, mosei_feature
    from image import ckplus
else:
    from .mm import iemocap_raw, iemocap_feature, meld_feature, mosei_feature
    from .image import ckplus

log = Logger()

regist_data = {

    # deprecated temporarily
    # 'ckplus-7': ckplus.ckplus,
    # 'iemocap-audio-raw-9': iemocap_raw.iemocap_audio,
    #
    # 'iemocap-audio-4': iemocap_raw.iemocap_audio_subset('4'),
    # 'iemocap-audio-v1-4': iemocap_raw.iemocap_audio_subset('4.1'),
    # 'iemocap-audio-6': iemocap_raw.iemocap_audio_subset('6'),
    #
    # 'iemocap-text-4': iemocap_raw.iemocap_text_subset('4'),
    # 'iemocap-text-v1-4': iemocap_raw.iemocap_text_subset('4.1'),
    # 'iemocap-text-6': iemocap_raw.iemocap_text_subset('6'),
    #
    # 'iemocap-ta-4': iemocap_raw.iemocap_text_audio_subset('4'),
    # 'iemocap-ta-v1-4': iemocap_raw.iemocap_text_audio_subset('4.1'),
    # 'iemocap-ta-6': iemocap_raw.iemocap_text_audio_subset('6'),
    # 'iemocap-mmin-4': iemocap_feature.iemocap_mmin_4,
    # deprecated temporarily

    'iemocap-cogmen-6': partial(iemocap_feature.iemocap_cogmen_6),
    # change text feature
    'iemocap-cogmen-sbert-6': partial(iemocap_feature.iemocap_cogmen_6, text='sbert'),
    'iemocap-cogmen-robert-6': partial(iemocap_feature.iemocap_cogmen_6, text='robert'),
    # change visual feature
    'iemocap-cogmen-tsn-6': partial(iemocap_feature.iemocap_cogmen_6, visual='tsn'),
    'iemocap-cogmen-tsn-v+-6': partial(iemocap_feature.iemocap_cogmen_6, visual='tsn+'),
    # change text and visual feature
    'iemocap-cogmen-sbert-tsn-6': partial(iemocap_feature.iemocap_cogmen_6, text='sbert', visual='tsn'),
    'iemocap-cogmen-robert-tsn-6': partial(iemocap_feature.iemocap_cogmen_6, text='robert', visual='tsn'),
    'iemocap-cogmen-sbert-tsn-v+-6': partial(iemocap_feature.iemocap_cogmen_6, text='sbert', visual='tsn+'),
    'iemocap-cogmen-robert-tsn-v+-6': partial(iemocap_feature.iemocap_cogmen_6, text='robert', visual='tsn+'),

    'iemocap-cogmen-4': partial(iemocap_feature.iemocap_cogmen_4),
    # change text feature
    'iemocap-cogmen-sbert-4': partial(iemocap_feature.iemocap_cogmen_4, text='sbert'),
    'iemocap-cogmen-robert-4': partial(iemocap_feature.iemocap_cogmen_4, text='robert'),
    # change visual feature
    'iemocap-cogmen-tsn-4': partial(iemocap_feature.iemocap_cogmen_4, visual='tsn'),
    'iemocap-cogmen-tsnss-4': partial(iemocap_feature.iemocap_cogmen_4, visual='tsnss'),
    'iemocap-cogmen-tsn-v+-4': partial(iemocap_feature.iemocap_cogmen_4, visual='tsn+'),
    'iemocap-cogmen-tsnss-v+-4': partial(iemocap_feature.iemocap_cogmen_4, visual='tsnss+'),
    # change text and visual feature
    'iemocap-cogmen-sbert-tsn-4': partial(iemocap_feature.iemocap_cogmen_4, text='sbert', visual='tsn'),
    'iemocap-cogmen-robert-tsn-4': partial(iemocap_feature.iemocap_cogmen_4, text='robert', visual='tsn'),
    'iemocap-cogmen-sbert-tsn-v+-4': partial(iemocap_feature.iemocap_cogmen_4, text='sbert', visual='tsn+'),
    'iemocap-cogmen-robert-tsn-v+-4': partial(iemocap_feature.iemocap_cogmen_4, text='robert', visual='tsn+'),
    'iemocap-cogmen-sbert-tsnss-4': partial(iemocap_feature.iemocap_cogmen_4, text='sbert', visual='tsnss'),
    'iemocap-cogmen-robert-tsnss-4': partial(iemocap_feature.iemocap_cogmen_4, text='robert', visual='tsnss'),
    'iemocap-cogmen-sbert-tsnss-v+-4': partial(iemocap_feature.iemocap_cogmen_4, text='sbert', visual='tsnss+'),
    'iemocap-cogmen-robert-tsnss-v+-4': partial(iemocap_feature.iemocap_cogmen_4, text='robert', visual='tsnss+'),

    'meld-mmgcn-7': partial(meld_feature.meld_mmgcn_7, text=None),
    'meld-mmgcn-sbert-7': partial(meld_feature.meld_mmgcn_7, text='sbert'),

    # used for extract text feature
    'iemocap-cogmen-text-4': partial(iemocap_feature.text_cogmen, n_class=4),
    'iemocap-cogmen-text-6': partial(iemocap_feature.text_cogmen, n_class=6),
    'meld-mmgcn-text-7': meld_feature.meld_mmgcn_text,

    # used for extract video feature
    'iemocap-cogmen-video-4': partial(iemocap_feature.video_cogmen, n_class=4),
    'iemocap-cogmen-video-6': partial(iemocap_feature.video_cogmen, n_class=6),

    "mosei-text-any-7": partial(mosei_feature.mosei_text),
    "mosei-interval-any-7": partial(mosei_feature.mosei_interval),

    "mosei-cim-2": partial(mosei_feature.mosei_cim),

    "mosei-emo-sbert-6": partial(mosei_feature.mosei_adapted, text='sbert'),
    "mosei-sent-sbert-7": partial(mosei_feature.mosei_adapted, text='sbert', label_type='sent_7'),
    "mosei-sent-sbert-2": partial(mosei_feature.mosei_adapted, text='sbert', label_type='sent_2'),

    "mosei-multi-sbert-fbank-6": partial(mosei_feature.mosei_adapted,
                                         text='sbert', audio='fbank', label_type='multi'),

    "mosei-emo-sbert-fbank-6": partial(mosei_feature.mosei_adapted,
                                       text='sbert', audio='fbank', label_type='emo'),
    "mosei-emo-sbert-fbank-blc-6": partial(mosei_feature.mosei_adapted,
                                           text='sbert', audio='fbank', label_type='emo', balance=True),

    "mosei-sent-sbert-fbank-7": partial(mosei_feature.mosei_adapted,
                                        text='sbert', audio='fbank', label_type='sent_7'),
    "mosei-sent-sbert-fbank-2": partial(mosei_feature.mosei_adapted,
                                        text='sbert', audio='fbank', label_type='sent_2'),
    "mosei-sent-sbert-fbank-+-2": partial(mosei_feature.mosei_adapted,
                                          text='sbert', audio='fbank', label_type='sent_2+'),

    "mosei-emo-sbert-is10-6": partial(mosei_feature.mosei_adapted,
                                      text='sbert', audio='is10', label_type='emo'),
    "mosei-sent-sbert-is10-7": partial(mosei_feature.mosei_adapted,
                                       text='sbert', audio='is10', label_type='sent_7'),
    "mosei-sent-sbert-is10-2": partial(mosei_feature.mosei_adapted,
                                       text='sbert', audio='is10', label_type='sent_2'),
    "mosei-sent-sbert-is10-+-2": partial(mosei_feature.mosei_adapted,
                                         text='sbert', audio='is10', label_type='sent_2+'),

    # "mosei-emo-pad80-6": partial(mosei_feature.mosei_unaligned, audio='pad80', label_type='emo'),
    # "mosei-sent-pad80-7": partial(mosei_feature.mosei_unaligned, audio='pad80', label_type='sent_7'),
    # "mosei-sent-pad80-2": partial(mosei_feature.mosei_unaligned, audio='pad80', label_type='sent_2'),
}


def pick_datas(root, dataset_name: str, split='train'):
    data_fn = regist_data.get(dataset_name, None)
    assert data_fn is not None
    res = data_fn(root, split=split)
    return res


if __name__ == '__main__':
    pick_datas('/Users/yhz/Downloads/IEMOCAP/', 'iemocap-cogmen-tsn-4')
