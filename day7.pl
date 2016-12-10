#!/usr/bin/env perl

# perl solution for day 7 part 1
use strict;
use warnings;

use File::Slurp;

sub found_abba {
  return 1 if $_[0] =~ /(.)(?!\1)(.)\2\1/;
  return 0;
}

sub supports_tls {
  my $input = $_[0];
  my $tls = found_abba($input);

  while ($input =~ /(\[.*?\])/g) {
    if (found_abba($1)) {
      $tls = 0;
    }
  }
  return $tls;
}

my @ips = read_file('input.txt');
my $total = 0;

foreach my $ip (@ips) {
  if (supports_tls($ip)) {
    $total += 1;
  }
}

print "$total\n"
