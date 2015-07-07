# -*- coding: utf-8 -*-
"""
.. module:: convert_xradia.py
   :platform: Unix
   :synopsis: Convert xradia files in data exchange.

Example on how to use the `xtomo_raw`_ module to read xradia raw tomographic data and save them as Data Exchange

:Author:
  `Francesco De Carlo <mailto: decarlof@gmail.com>`_

:Organization:
  Argonne National Laboratory, Argonne, IL 60439 USA

:Version: 2014.08.15

.. _xtomo_raw: dataexchange.xtomo.xtomo_importer.html
"""

# Data Exchange: https://github.com/data-exchange/data-exchange
import xtomo_importer as xtomo_imp 
import xtomo_exporter as xtomo_exp

import olefile as olef
import struct


def read_meta_txm(file_name, meta_data_name=None):

    try:
        olef.isOleFile(file_name)
        
        meta_data= None
        ole = olef.OleFileIO(file_name)
        if ole.exists('ImageInfo/NoOfImages'):                  
            stream = ole.openstream('ImageInfo/NoOfImages')
            data = stream.read()
            n_images = struct.unpack('<I', data)
            number_of_images = n_images[0]

            if ole.exists(meta_data_name):
                print 'Reading: [%s].' % meta_data_name
                stream = ole.openstream(meta_data_name)
                data = stream.read()
                if (meta_data_name == 'ImageInfo/Date'):
                    meta_data = struct.unpack('<'+'17s23x'*number_of_images, data)
                else:
                    struct_fmt = "<{}f".format(number_of_images)
                    meta_data = struct.unpack(struct_fmt, data)            
            ole.close()

    except KeyError:
        print 'Reading: [%s] failed.' % file_name
        meta_data = None

    return meta_data

def main():

    file_name = '/local/dataraid/databank/templates/xradia_dtu/sample_name.txrm'
    hdf5_file_name = '/local/dataraid/databank/templates/dataExchange/tmp/DTU.h5'
    sample_name = 'halvmaane_150kV-HE6-20X-60s'

    experimenter_name="Martin Skovgaard Andersen"
    experimenter_affiliation="Technical University of Denmark" 
    experimenter_email="mskan@dtu.dk"
    instrument_comment="Xradia Versa micro CT scanner"  

    image_exposure_time = read_meta_txm(file_name,'ImageInfo/ExpTimes')
    image_time = read_meta_txm(file_name,'ImageInfo/Date')
    image_theta = read_meta_txm(file_name,'ImageInfo/Angles')
    sample_image_shift_x = read_meta_txm(file_name,'Alignment/X-Shifts')
    sample_image_shift_y = read_meta_txm(file_name,'Alignment/Y-Shifts')
    sample_position_x = read_meta_txm(file_name,'ImageInfo/XPosition')
    sample_position_y = read_meta_txm(file_name,'ImageInfo/YPosition')
    sample_position_z = read_meta_txm(file_name,'ImageInfo/ZPosition')

    # Read raw data
    read = xtomo_imp.Import()
    data, white, dark, theta = read.xtomo_raw(file_name, data_type='xradia', log='INFO')
   
    # Save data as dataExchange
    write = xtomo_exp.Export()
    write.xtomo_exchange(data = data,
                          data_white = white,
                          data_dark = dark,
                          theta = theta,
                          hdf5_file_name = hdf5_file_name,
                          experimenter_name=experimenter_name, 
                          experimenter_affiliation=experimenter_affiliation, 
                          experimenter_email=experimenter_email, 
                          instrument_comment=instrument_comment,  
                          sample_name = sample_name,
                          sample_position_x = sample_position_x ,
                          sample_position_y = sample_position_y,
                          sample_position_z = sample_position_z,
                          sample_image_shift_x = sample_image_shift_x,
                          sample_image_shift_y = sample_image_shift_y,
                          image_exposure_time = image_exposure_time,
                          image_time = image_time,
                          image_theta = image_theta,
                          data_exchange_type = 'tomography_raw_projections'
                          )

if __name__ == "__main__":
    main()

