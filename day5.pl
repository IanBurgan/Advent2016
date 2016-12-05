#!/usr/bin/env perl

# perl solution for part 1 of day 5 made after overwriting part 1 in python
use strict;
use warnings;

use Digest::MD5 qw/md5_hex/;

my $input = 'wtnhxymk';
my $count = 0;

my $ans = '';

my $hash = md5_hex($input, $count);

while (length ($ans) < 8) {
  if (substr($hash, 0, 5) eq '00000') {
    $ans .= substr($hash, 5, 1)
  }

  $count++;
  $hash = md5_hex($input, $count);
}

print $ans;
