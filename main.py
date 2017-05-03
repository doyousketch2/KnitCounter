#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##=========================================================
##  atlas.py                                    21 Apr 2017
##
##  Generates a Kivy Atlas from spritesheet
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

from kivy .app        import  App                   ##  GUI
from kivy .uix .widget  import Widget

##=========================================================
##  script  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



class RootWidget(Widget):


  def column(self, x):
    KnitCount .column += x
    if KnitCount .column < 1:
      KnitCount .column = 0
    KnitCount .colstr = str(KnitCount .column)
    self .ids .column .text = KnitCount .colstr

  def row(self, y):
    KnitCount .row += y
    if KnitCount .row < 1:
      KnitCount .row = 0
    KnitCount .rowstr = str(KnitCount .row)
    self .ids .row .text = KnitCount .rowstr


class KnitCount(App):
  icon  = 'icon.png'
  title  = "Knit Counter  ::  by Doyousketch2"

  column = 0
  row    = 0
  colstr = '0'
  rowstr = '0'

  def build(self):
    pass


##=========================================================
##  main  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
  KnitCount() .run()


##=========================================================
##  eof  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

