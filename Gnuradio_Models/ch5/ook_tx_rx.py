#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: OOK  TX RX
# Author: parallels
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from OOK_mod import OOK_mod  # grc-generated hier_block
from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class ook_tx_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "OOK  TX RX", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("OOK  TX RX")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ook_tx_rx")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.working_samp_rate = working_samp_rate = 400e3
        self.threshold = threshold = 500
        self.samp_rate = samp_rate = 8e5
        self.noise_level = noise_level = 2000
        self.gain = gain = 1e3
        self.filter_transition = filter_transition = 1e3
        self.filter_cutoff = filter_cutoff = 50e3
        self.center_freq = center_freq = 40e3

        ##################################################
        # Blocks
        ##################################################
        self._threshold_tool_bar = Qt.QToolBar(self)
        self._threshold_tool_bar.addWidget(Qt.QLabel("'threshold'" + ": "))
        self._threshold_line_edit = Qt.QLineEdit(str(self.threshold))
        self._threshold_tool_bar.addWidget(self._threshold_line_edit)
        self._threshold_line_edit.returnPressed.connect(
            lambda: self.set_threshold(eng_notation.str_to_num(str(self._threshold_line_edit.text()))))
        self.top_layout.addWidget(self._threshold_tool_bar)
        self._noise_level_range = Range(10e-4, 10000, 1, 2000, 200)
        self._noise_level_win = RangeWidget(self._noise_level_range, self.set_noise_level, "'noise_level'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_level_win)
        self.qtgui_time_sink_x_0_0_0_1_0_0 = qtgui.time_sink_f(
            int(16384/100), #size
            1/0.25e-3, #samp_rate
            "Xor output", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_1_0_0.set_y_axis(-0.1, 1.5)

        self.qtgui_time_sink_x_0_0_0_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_1_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.5, 1e-3, 0, "")
        self.qtgui_time_sink_x_0_0_0_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_1_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_1_0_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 0, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [0, 0, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 7, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_1_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_1_0_0_win)
        self.qtgui_time_sink_x_0_0_0_1_0 = qtgui.time_sink_f(
            int(16384/100), #size
            1/0.25e-3, #samp_rate
            "Decimated Baseband", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_1_0.set_y_axis(-0.1, 1.5)

        self.qtgui_time_sink_x_0_0_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_1_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.5, 1e-3, 0, "")
        self.qtgui_time_sink_x_0_0_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0_1_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 0, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [0, 0, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 7, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_1_0_win)
        self.qtgui_number_sink_0_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_0_1.set_title("Xor count")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_1.set_min(i, -100)
            self.qtgui_number_sink_0_0_1.set_max(i, 200)
            self.qtgui_number_sink_0_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_1.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_1_win)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title("RMS Signal")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0.set_min(i, -100)
            self.qtgui_number_sink_0_0_0.set_max(i, 200)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("SNR (dB)")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0.set_min(i, -100)
            self.qtgui_number_sink_0_0.set_max(i, 200)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_xor_xx_0 = blocks.xor_bb()
        self.blocks_vector_source_x_0 = blocks.vector_source_f((0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0), True, 1, [])
        self.blocks_uchar_to_float_1 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_rms_xx_0 = blocks.rms_cf(0.0001)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(20, 1, 0)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, 800)
        self.blocks_integrate_xx_0 = blocks.integrate_ff(1000000, 1)
        self.blocks_float_to_uchar_1_0 = blocks.float_to_uchar()
        self.blocks_float_to_uchar_1 = blocks.float_to_uchar()
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(-1*threshold)
        self.band_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                35e3,
                45e3,
                2e3,
                window.WIN_HAMMING,
                6.76))
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_level, 0)
        self.analog_const_source_x_1_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 692)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, noise_level)
        self.OOK_mod_1 = OOK_mod(
            gain=0,
            interpolation=0,
            samp_rate=0,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.OOK_mod_1, 0), (self.band_pass_filter_0, 0))
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.analog_const_source_x_1_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_float_to_uchar_1, 0), (self.blocks_xor_xx_0, 0))
        self.connect((self.blocks_float_to_uchar_1_0, 0), (self.blocks_xor_xx_0, 1))
        self.connect((self.blocks_integrate_xx_0, 0), (self.qtgui_number_sink_0_0_1, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_float_to_uchar_1, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.qtgui_time_sink_x_0_0_0_1_0, 1))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.qtgui_number_sink_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_uchar_to_float_1, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_uchar_to_float_1, 0), (self.qtgui_time_sink_x_0_0_0_1_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.OOK_mod_1, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_float_to_uchar_1_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.qtgui_time_sink_x_0_0_0_1_0, 0))
        self.connect((self.blocks_xor_xx_0, 0), (self.blocks_uchar_to_float_1, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_uchar_to_float_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ook_tx_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_working_samp_rate(self):
        return self.working_samp_rate

    def set_working_samp_rate(self, working_samp_rate):
        self.working_samp_rate = working_samp_rate

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        Qt.QMetaObject.invokeMethod(self._threshold_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.threshold)))
        self.blocks_add_const_vxx_0.set_k(-1*self.threshold)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 35e3, 45e3, 2e3, window.WIN_HAMMING, 6.76))

    def get_noise_level(self):
        return self.noise_level

    def set_noise_level(self, noise_level):
        self.noise_level = noise_level
        self.analog_const_source_x_1.set_offset(self.noise_level)
        self.analog_noise_source_x_0.set_amplitude(self.noise_level)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_filter_transition(self):
        return self.filter_transition

    def set_filter_transition(self, filter_transition):
        self.filter_transition = filter_transition

    def get_filter_cutoff(self):
        return self.filter_cutoff

    def set_filter_cutoff(self, filter_cutoff):
        self.filter_cutoff = filter_cutoff

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq




def main(top_block_cls=ook_tx_rx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
