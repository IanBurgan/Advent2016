#!/usr/bin/env perl

# Perl solution for part 1 of day 2 made after overwriting part 1 in python
use strict;
use warnings;

use File::Slurp;

my @lines = read_file('input.txt');

my $buttons = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

my @pos = (1, 1);

foreach my $line (@lines) {
  chomp $line;
  my @moves = split //, $line;

  foreach my $move (@moves) {
    $pos[0] -= 1 if $move eq "U";
    $pos[0] += 1 if $move eq "D";
    $pos[1] -= 1 if $move eq "L";
    $pos[1] += 1 if $move eq "R";

    $pos[0] = 0 if $pos[0] < 0;
    $pos[0] = 2 if $pos[0] > 2;
    $pos[1] = 0 if $pos[1] < 0;
    $pos[1] = 2 if $pos[1] > 2;
  }

  print $buttons->[$pos[0]][$pos[1]]
}

print "\n"
