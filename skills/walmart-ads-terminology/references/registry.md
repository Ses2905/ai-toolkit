# Terminology Registry

**Status of this file: seeded draft. Nothing here is confirmed canon yet.**

Every entry below is marked `unverified` — drawn from public/industry usage,
not from Walmart's internal source of truth. Until an entry is marked
`canonical` with a real `source`, treat it as a starting point for
confirmation, not as an answer. See *Filling this in* at the bottom.

## Entry template

```
### <Canonical term>
- **status**: canonical | provisional | deprecated | unverified
- **means**: one sentence, in advertiser-facing language
- **not**: terms it is confused with, and why they differ
- **avoid**: deprecated or internal-only variants that must not ship
- **surfaces**: where it appears (UI, API, reporting, help, sales collateral)
- **source**: who decided, and where that decision is written down
- **transition**: if renaming — the old name, and the date the crutch retires
```

Fields exist to prevent specific failures. `not` stops two adjacent concepts
collapsing into one word. `avoid` is what makes an audit mechanical rather than
a matter of taste. `source` is what lets a future reader check the claim instead
of trusting it.

---

## Organization & platform

### Walmart Connect
- **status**: unverified
- **means**: Walmart's advertising business and the brand advertisers buy through.
- **avoid**: Walmart Media Group (prior name), WMG, "Walmart Ads" as a proper noun in advertiser-facing copy
- **surfaces**: all advertiser-facing
- **source**: public brand usage — CONFIRM internal style guidance

### Walmart Global Ads
- **status**: unverified
- **means**: the internal organization. Internal-facing only.
- **not**: Walmart Connect — the org is not the advertiser-facing brand
- **avoid**: using this in anything an advertiser reads
- **source**: CONFIRM

---

## Ad products

Seeded from publicly marketed product names. Each needs confirmation of exact
capitalization, whether it is singular or plural in UI, and whether the
advertiser-facing name matches the internal one.

### Sponsored Products
- **status**: unverified
- **means**: keyword- and item-targeted ads placed in search and browse results.
- **source**: public product naming — CONFIRM

### Sponsored Brands
- **status**: unverified
- **means**: banner-style ads featuring a brand logo, headline, and multiple items.
- **source**: public product naming — CONFIRM

### Sponsored Videos
- **status**: unverified
- **means**: video ad format in search results.
- **source**: public product naming — CONFIRM

### Display
- **status**: unverified
- **means**: non-sponsored-listing placements, onsite and offsite.
- **not**: Sponsored Brands — which is a sponsored-listing format despite being visual
- **source**: CONFIRM — also confirm whether onsite/offsite are separate named products

### Walmart DSP
- **status**: unverified
- **means**: the self-serve demand-side platform for programmatic buying.
- **source**: public product naming — CONFIRM

---

## Advertiser types

The distinction that most often goes wrong in specs, because "advertiser" gets
used as though it were one audience when the two have different entitlements,
workflows, and support paths.

### Marketplace seller
- **status**: unverified
- **means**: a third-party seller advertising their own listings.
- **not**: supplier/1P brand — different onboarding, catalog, and billing
- **source**: CONFIRM exact preferred term (seller / marketplace seller / 3P seller)

### Supplier
- **status**: unverified
- **means**: a first-party brand whose items Walmart buys and resells.
- **not**: marketplace seller
- **avoid**: "vendor" if internal style prefers supplier
- **source**: CONFIRM

---

## Metrics

**Do not assert a Walmart calculation from memory.** The names below are
industry-standard; the *definitions* — attribution window, what counts as a
conversion, in-store inclusion — are Walmart methodology decisions and must be
sourced, never inferred.

### ROAS
- **status**: unverified
- **means**: return on ad spend.
- **source**: CONFIRM — attribution window and whether in-store sales are included

### New-to-brand (NTB)
- **status**: unverified
- **means**: purchases from customers who have not bought the brand in a defined lookback.
- **source**: CONFIRM — lookback length is the whole definition and must not be guessed

---

## Deprecated

Terms that must not ship. Empty until a rename is actually decided — an
aspirational deprecation list teaches people to ignore the registry.

_(none confirmed yet)_

---

## Filling this in

The fastest path from this draft to something trustworthy:

1. **Harvest, do not author.** Pull the terms already used in the campaign
   creation flow, the reporting export column headers, the API reference, and
   the help center. Those four disagreeing with each other *is* the finding.
2. **Start with conflicts, not coverage.** A registry of 200 uncontested terms
   is busywork. The twenty terms where surfaces disagree are the whole value.
3. **Mark status honestly.** `provisional` is a useful, respectable state.
   Marking everything `canonical` to look finished destroys the file's
   usefulness, because a reader can no longer tell what is actually settled.
4. **Record the source every time.** An entry without one cannot be defended
   when someone senior disagrees in a review.
