#!/usr/bin/perl -w

use strict;

my $c = 1;
while(<STDIN>){
  #regex matches only pos. int
  die "Wrong input: expect two ints got $_" unless /(\d+)\s+(\d+)\s*/;
  my $lines=$1;
  my $rows=$2;
  if ($lines == 0 && $rows == 0){
    exit 0;
  }
  die "Wrong input: expect two pos ints  or 0 0 got $_" unless ($lines > 0 && $rows > 0);
  die "Wrong input: expect two pos ints smaller 100 got $_" unless ($lines < 101 && $rows < 101);
  my @field;
  my @output;
  for (my $k=0;$k<$lines;$k++){
    $_=<STDIN>;
    die "Wrong input: needed * . or space got $_" unless /[*. ]*/;
    my @field2=split(/\s+/);   
    die "Wrong input: expected $rows fields, got ",$#field2+1," fields in $_" unless ($#field2+1 == $rows);
    $field[$k]=\@field2;
    for (my $l=0;$l<$rows;$l++){
      $output[$k+1][$l+1]=0;
    }
  }
  for (my $k=0;$k<$lines;$k++){
    for (my $l=0;$l<$rows;$l++){
      if ($field[$k][$l] eq "*"){
	#loop over nbs, self doesn't matter, overwritten below
	for (my $i=0;$i<3;$i++){
	  for (my $j=0;$j<3;$j++){
	    $output[$k+$i][$l+$j]++;
	  }
	}
      } elsif ($field[$k][$l] ne ".") {
	die "Wrong input: expected * or ., got $field[$k][$l]";
      }
    }
  }

  #Override mines
  for (my $k=0;$k<$lines;$k++){
    for (my $l=0;$l<$rows;$l++){
      if ($field[$k][$l] eq "*"){
	$output[$k+1][$l+1]="*";
      }
    }
  }

  #output
  print "Field #",$c++,":\n";
  for (my $k=0;$k<$lines;$k++){
    for (my $l=0;$l<$rows;$l++){
      print "$output[$k+1][$l+1] ";
    }
    print "\n";
  }
  print "\n";
}
