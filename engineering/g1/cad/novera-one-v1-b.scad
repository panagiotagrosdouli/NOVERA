// NOVERA ONE V1 — Candidate B, conceptual parametric CAD envelope
// Units mm. NOT engineering-approved, printable, manufacturable or safety validated.
// OpenSCAD: openscad -o novera-one-v1-b.stl novera-one-v1-b.scad
$fn = 48;
H = 1050; W = 500; D = 500;
base_h = 170; deck_z = 90;
wheel_r = 76; wheel_thick = 42; wheel_x = 191; wheel_y = 0; wheel_z = 86;
body_w = 272; body_d = 235; body_bottom = 175; body_top = 800;
head_w = 325; head_d = 145; head_h = 190; head_z = 860;
module rounded_box(sz,r) {
  minkowski() {
    cube([sz[0]-2*r,sz[1]-2*r,sz[2]-2*r],center=true);
    sphere(r=r,$fn=20);
  }
}
module base_chassis() {
  color([0.77,0.82,0.88]) translate([0,0,base_h/2])
    rounded_box([W-32,D-32,base_h],30);
  // Battery is purely a packaging placeholder, not a chosen battery.
  color([0.16,0.2,0.26]) translate([0,-35,110])
    cube([245,170,95],center=true);
}
module drivetrain() {
  for (x=[-wheel_x,wheel_x]) {
    color([0.12,0.15,0.2]) translate([x,wheel_y,wheel_z])
      rotate([0,90,0]) cylinder(r=wheel_r,h=wheel_thick,center=true);
  }
  // Schematic stabilizer casters — actual 4-contact support needs analysis.
  for (y=[-173,173]) {
    color([0.2,0.25,0.29]) translate([0,y,36]) sphere(r=35);
  }
}
module torso() {
  color([0.9,0.93,0.96]) translate([0,0,(body_bottom+body_top)/2])
    rounded_box([body_w,body_d,body_top-body_bottom],35);
  // Computer and power enclosure reserved volumes, not real parts.
  color([0.25,0.31,0.4]) translate([0,0,330])
    cube([190,150,115],center=true);
  color([0.12,0.17,0.23]) translate([0,-body_d/2-6,600])
    cube([190,12,230],center=true);
}
module head() {
  color([0.9,0.94,0.97]) translate([0,0,head_z+head_h/2])
    rounded_box([head_w,head_d,head_h],28);
  color([0.06,0.1,0.16]) translate([0,-head_d/2-5,head_z+head_h/2])
    cube([275,12,134],center=true);
}
module model() {
  base_chassis();
  drivetrain();
  torso();
  head();
}
model();
