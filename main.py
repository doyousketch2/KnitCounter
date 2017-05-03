#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##=========================================================
##  main.py                                    21 Apr 2017
##
##  Row-counter for crochet & knitting
##
##  Eli Leigh Innis
##  Twitter :  @ Doyousketch2
##  Email :  Doyousketch2 @ yahoo.com
##
##  GNU GPLv3                 gnu.org/licenses/gpl-3.0.html
##=========================================================
##  required  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##  you'll need kivy:
##  (debian)
##        sudo pip3 install kivy
##  (linux)
##        sudo python3 -m pip install kivy
##  (mac)
##        sudo easy_install pip
##        python -m pip install kivy
##  (win)
##        py -m pip install kivy
##=========================================================
##  libs  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from kivy .app          import  App                 ##  GUI
from kivy .uix .widget  import Widget
from kivy .config       import Config

##=========================================================
##  script  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class RootWidget(Widget):

  def row(self, x):
    KnitCount .row += x
    if KnitCount .row < 1:
      KnitCount .row  = 0
    KnitCount .rowstr  = str(KnitCount .row)

    Config .set('settings',  'row',  KnitCount .row)
    Config .write()

    self .ids .row .text  = KnitCount .rowstr


class KnitCount(App):
  icon  = 'icon.png'
  title  = "Knit Counter  ::  by Doyousketch2"

  Config .read('config.ini')

  row  = Config .getint('settings', 'row')
  rowstr  = str(row)

  def build(self):
    pass



##=========================================================
##  main  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
  KnitCount() .run()


##=========================================================
##  eof  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
