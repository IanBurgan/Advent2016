#!/usr/bin/env perl

# perl solution for day 14 part 1
use strict;
use warnings;

use Digest::MD5 'md5_hex';

my $salt = 'qzyelonm';
my $count = -1;

my $keys = 0;

while ($keys < 64) {
  $count++;
  my $hash = md5_hex($salt, $count);

  if ($hash =~ /(.)\1\1/) {
    my $match = $1;
    my $found = 0;

    for my $i (1 .. 1000) {
      $hash = md5_hex($salt, $count + $i);
      if ($hash =~ /$match{5}/) {
        $found = 1;
      }
    }
    $keys++ if $found;
  }
}

print "$count\n";
