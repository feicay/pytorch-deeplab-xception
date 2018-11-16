class Path(object):
    @staticmethod
    def db_root_dir(database):
        if database == 'pascal':
            return '/path/to/Segmentation/VOCdevkit/VOC2012/'  # folder that contains VOCdevkit/.
        elif database == 'sbd':
            return '/path/to/Segmentation/benchmark_RELEASE/' # folder that contains dataset/.
        elif database == 'cityscapes':
            return '/home/adas/data/cityscapes'         # foler that contains leftImg8bit/
        elif database == 'bdd_drivable':
            return '/home/adas/data/bdd100k'
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError
