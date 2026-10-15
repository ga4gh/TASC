# Reference sequence names

**Source**: TASC  
**Recommendation**: TBD  
**Title**: Reference sequence names  
**Related GitHub issues**: [TASC #5](https://github.com/ga4gh/TASC/issues/5)  
**Author**: John Marshall  
**Status:** Draft


## Abstract

This recommendation standardises a set of ASCII characters considered valid in reference sequence or contig names.
In particular it identifies characters not considered valid that are safe for use as delimiters around such names in text formats.
Protocols, file formats, and other standards that adhere to this recommendation enable easy interoperability for their reference sequence names.


## Recommendation

The names or identifiers of reference sequences, chromosomes, or contigs MUST match the following regular expression:

    [0-9A-Za-z!#$%&+./:;?@^_|~-][0-9A-Za-z!#$%&*+./:;=?@^_|~-]*

Equivalently, these names or identifiers adhere to the following rules:

* Each character in a name MUST be a printable ASCII character that is either numeric (`0-9`), alphabetical (`A-Z` or `a-z`), or one of the punctuation characters `!#$%&*+-./:;=?@^_|~`
* Hence space (and other whitespace), quote (`"` `'` and grave accent/backquote), bracket (`()[]{}<>`), comma (`,`), and backslash (`\`) characters MUST NOT appear within a name.
* Additionally the first character of a name MUST NOT be an asterisk or equals sign (`*=`).


## Background

Reference sequences are fundamental to genomic analysis and interpretation.
Many GA4GH formats and protocols need to refer to reference sequences, which is often done by way of a _name_ or _identifier_ referring to a reference sequence:

* In the [SAM, BAM][sam], and [CRAM][] file formats, names appear in the `@SQ-SN` header field, the `RNAME`/`RNEXT` fields, and are embedded in `CC`, `OA`, and `SA` tagged field values.
* In the [VCF][] file format, names appear in the `##contig` header, the `CHROM` field, and breakend notation.
* In the [BED][] file format, names appear as the `chrom` field.
* In the [htsget][] protocol, names appear as a `referenceName` URL query parameter and as a JSON string in POST request bodies.
* In the [refget sequences][refget] protocol, names may be returned as an `alias` encoded as a JSON string.

For protocols that represent their data in a format such as JSON that quotes the name as a "string" and provides an escape mechanism, arbitrary names can be represented.
Hence those protocols themselves do not require restrictions on valid name characters.
But bioinformatics largely runs on ad-hoc text formats, and many of those that are in widespread use various unquoted fields without escape mechanisms, so do require such restrictions.
Hence GA4GH promotes a lowest-common-denominator restricted set of characters valid in names for the sake of interoperability.

### Constraints on particular characters

The classic reference sequence name is probably `1` or `chr1`.
Hence clearly alphanumeric characters `A-Z a-z 0-9` need to be considered valid.
(For ease of implementation, names are generally considered to be **case-sensitive**.)
For historic reasons and to avoid questions around character encoding, it is reasonable to restrict names to [ASCII][] characters.

The [SAM][] file format embeds reference sequence names in both header and record fields:

    @SQ   SN:chr1   LN:248956422
    r1    0   chr1  10000   10   4M   *   0   0   ATGC    QQQQ    SA:Z:chr1,20000,+,4M,15,0;

Because SAM does not define an escaping mechanism, this means that tab characters must not appear in names and commas must not appear in names if they are to be used in `OA` or `SA` tagged fields---and it's best to simplify that to "commas must not appear at all".
(The SAM format's `RNAME` and `RNEXT` fields reserve values starting with `*` and `=` for special purposes, hence this recommendation's corresponding restriction on a name's first character.)

The [VCF][] file format generally refers to these names as "contigs" and embeds them in headers and records:

    ##contig=<ID=chr1,length=248956422>
    #CHROM   POS   ID   REF   ALT   QUAL   FILTER   INFO
    chr1     10000 .    A     T     10     PASS     .

Thus VCF must similarly forbid tabs and commas.

In the [htsget][] protocol, reference sequence names appear in URLs:

    https://example.org/htsget/reads/SAMPLE1?referenceName=chr1&start=9999&end=20000

There may be a case to discourage non-URL-safe characters in names, `&` in particular, but because characters can be percent-encoded there is an escape mechanism.


## Considerations

Some programs use notation such as `chr1:10000-20000` to indicate a particular region on a reference sequence.
This notation can be difficult to parse when used with reference sequence names that themselves contain colon
characters.
It may be tempting to forbid or fail to process such reference sequence names, but this would be unwise as e.g. the standard nomenclature for HLA alleles uses colons heavily.
Appendix A of the [SAM specification][sam] recommends approaches for parsing region notation when the reference sequence name itself contains colon characters.

Whitespace and the punctuation characters that are invalid (notably comma and the various brackets) were considered to be desirable for use as delimiters around reference sequence names and identifiers.
Similarly backslash was considered to be commonly desirable as an escape character.
Making these invalid in names was supported by a survey of extant reference sequence names in several sequence archives, where their use was vanishingly rare.


## References

1. [BED][], [CRAM][], [htsget][], [Refget Sequences][refget], [Refget Sequence Collections][seqcol], [SAM][], [VCF][] --- File format and protocol specifications.
1. [hts-specs PR #333](https://github.com/samtools/hts-specs/pull/333) --- Survey of punctuation characters in reference sequence names in sequence archives.

[ascii]:    https://en.wikipedia.org/wiki/ASCII
[bed]:      https://samtools.github.io/hts-specs/BEDv1.pdf
[cram]:     https://samtools.github.io/hts-specs/CRAMv3.pdf
[htsget]:   https://samtools.github.io/hts-specs/htsget.html
[refget]:   https://ga4gh.github.io/refget/sequences/
[sam]:      https://samtools.github.io/hts-specs/SAMv1.pdf
[seqcol]:   https://ga4gh.github.io/refget/seqcols/
[vcf]:      https://samtools.github.io/hts-specs/VCFv4.5.pdf


## Contributors

<!-- Need to fill in here with all contributors and reviewers who have provided input. Contributions should be matched against [CRediT](https://credit.niso.org/). -->

John Marshall: Investigation, Writing -- original draft
