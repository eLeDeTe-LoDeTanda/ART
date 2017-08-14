/*
 #Approximate render time calculator
 #Copyright (c) (2016) Marcelo "Tanda" Cerviño.
 #Argentina. 
 # http://lodetanda.blogspot.com -- lodetanda @ gmail.com
 
 # ***** BEGIN GPL LICENSE BLOCK *****
 #
 #
 # This program is free software; you can redistribute it and/or
 # modify it under the terms of the GNU General Public License
 # as published by the Free Software Foundation; either version 3
 # of the License, or (at your option) any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program; if not, write to the Free Software Foundation,
 # Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 #
 # ***** END GPL LICENCE BLOCK *****
 
 #ARTv1.0 -10/2016-.
 */

import controlP5.*;

ControlP5 cp5;

PImage background;

int time;
int frames;
int H;
int M;
int S;
int fps; 
int cpu;
int d;
int h;
int m;
int s;
int ah;
int am;
int as;

int aniDuration;

int offset_x= 25;
int offset_y= 130;

void setup() {
  size(323, 480);
  noStroke();

  background = loadImage("background.png");

  PFont font = createFont("arial", 14);

  cp5 = new ControlP5(this);

  cp5.addNumberbox("H")
    .setPosition(offset_x, offset_y)
    .setSize(40, 20)
    .setScrollSensitivity(1)
    .setFont(font)
    .setMin(0)
    .setValue(0)
    ;

  cp5.addNumberbox("M")
    .setPosition(offset_x+45, offset_y)
    .setSize(40, 20)
    .setScrollSensitivity(1)
    .setFont(font)
    .setRange(0, 60)
    .setValue(1)
    ;

  cp5.addNumberbox("S")
    .setPosition(offset_x+90, offset_y)
    .setSize(40, 20)
    .setScrollSensitivity(1)
    .setFont(font)
    .setRange(0, 60)
    .setValue(0)
    ;

  cp5.addNumberbox("frames")
    .setPosition(offset_x, offset_y+50)
    .setSize(70, 20)
    .setScrollSensitivity(1)
    .setFont(font)
    .setRange(1, 9999999)
    .setValue(240)
    ;

  cp5.addNumberbox("fps")
    .setPosition(offset_x, offset_y+100)
    .setSize(40, 20)
    .setScrollSensitivity(1)
    .setFont(font)
    .setRange(1, 999)
    .setValue(24)
    ;

  cp5.addNumberbox("cpu")
    .setPosition(offset_x, offset_y+150)
    .setSize(50, 20) 
    .setScrollSensitivity(1)
    .setFont(font)
    .setRange(1, 99999)
    .setValue(1)
    ;
}

void draw() {

  frameRate(6);
  background(background);

  if (S > 59) {
    Controller S = cp5.getController("S");
    S.setValue(0);
  }
  if (M > 59) {
    Controller c = cp5.getController("M");
    c.setValue(0);
  }
  if (cpu > frames) {
    Controller c = cp5.getController("cpu");
    c.setValue(frames);
  }


  fill(30, 140, 140);
  textSize(24);
  textAlign(CENTER);
  text("ART v1.0", width/2, 40);
  textSize(20);
  fill(190, 150, 10);
  text("Approximate Render Time", width/2, 65);
  fill(200, 40, 20);
  text(d+"d:"+h+"h:"+m+"m:"+s+"s", width/2, height-40);
  textSize(20);
  fill(0, 140, 217);
  text(ah+"h:"+am+"m:"+as+"s", width/2, height-90);
  textSize(16);
  fill(200);
  text("Approximate render time:", width/2, height-65);
  text("Time per frame:", offset_x + 68, offset_y - 15);
  textSize(14);
  text("Animation:", width/2, height-115);

  aniDuration = frames / fps;

  if (cpu > frames) {
    cpu = frames;
  }

  time = ((frames * (((H*60)+M)*60+S)) / cpu);

  s = time % 60;
  m = time/60;
  h = m / 60;
  m = m % 60;
  d = h / 24;
  h = h % 24;

  as = aniDuration % 60;
  am = aniDuration/60;
  ah = am / 60;
  am = am % 60;
}

void  mousePressed() {
  if (mouseButton == CENTER) {
    Controller c = cp5.getController("frames");
    if (c.isMouseOver())c.setValue(frames+100);
  }
  if (mouseButton == RIGHT) {
    Controller c = cp5.getController("frames");
    if (c.isMouseOver())c.setValue(frames-100);
  }
}