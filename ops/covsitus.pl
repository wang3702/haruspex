#!/usr/bin/perl
if(@ARGV!=1){
 print "$0 [file]\n";
 exit;
}

($file,$path)=@ARGV;


@B=firstfile("$file");

#C: Res= 75 d= 1.421 Window= 3 Step= 2.000000 Base= 71.297501 -6.645500 251.313507
#1.318000 9.226000 -13.179999 -64.582001 63 88 69
#

print "$B[0][8] $B[0][10] $B[0][11] $B[0][12]  $B[0][6] $B[0][6] $B[0][6]\n";
for($i=1;$i<=$B[0][6]*$B[0][6]*$B[0][6];$i++){
 printf("%f ",$B[1][$i]);
 if($i%10==0 && $i != 0){
  print"\n";
 }
}
print"\n";

#@key = sort { $hash{$a} <=> $hash{$b} || $a <=> $b} keys %hash;


sub firstfile{
my $cnt=0;
my @A;
open(IN,$_[0]) or die;
while(<IN>){
 chomp;
 my $item;
 @{$item}=split(/[,\s\t]+/,$_);
 push @A, $item
}
close(IN);
return @A;
}
sub onetothree{
 %amin123 = ("W"=>"TRP","F"=>"PHE","Y"=>"TYR","L"=>"LEU","I"=>"ILE","V"=>"VAL","M"=>"MET","A"=>"ALA","G"=>"GLY","P"=>"PRO","C"=>"CYS","T"=>"THR","S"=>"SER","Q"=>"GLN","N"=>"ASN","E"=>"GLU","D"=>"ASP","H"=>"HIS","K"=>"LYS","R"=>"ARG");
 %amin321 = ("TRP"=>"W","PHE"=>"F","TYR"=>"Y","LEU"=>"L","ILE"=>"I","VAL"=>"V","MET"=>"M","ALA"=>"A","GLY"=>"G","PRO"=>"P","CYS"=>"C","THR"=>"T","SER"=>"S","GLN"=>"Q","ASN"=>"N","GLU"=>"E","ASP"=>"D","HIS"=>"H","LYS"=>"K","ARG"=>"R");
}
sub firstfile_line{
my $cnt=0;
my @A;
open(IN,$_[0]) or die;
while(<IN>){
  next if(/^#/);
 chomp;
 push @A, $_;
}
close(IN);
return @A;
}

sub readpdb{
 my $cnt=0;
 my @A;
 my ($x,$y,$z);
 my ($file)=@_;

 open(IN,$file) or die;
 while(<IN>){
  next unless(/^ATOM/);
  chomp;

  $x=substr($_,30,8);
  $y=substr($_,38,8);
  $z=substr($_,46,8);

  my $atm=substr($_,13,3);
  my $res=substr($_,17,3);
  my $rnum=substr($_,22,4);
  #my $m_tag=substr($_,17,9);
  my $m_tag=substr($_,13,13);

  my $item;
  @{$item}=($res,$atm,$x,$y,$z,$rnum,$m_tag);
  push @A, $item;
 }
 close(IN);
 return @A;
}

