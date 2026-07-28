#!/usr/bin/env python3
"""Build city + suburb landing pages for Apollo Earthworks.

Mirrors the structure of /earthworks-melbourne/ (paid-LP style: minimal
nav, in-page form, in-page testimonial slot, Service+FAQ schema, no
fabricated trust signals). Each generated page lives in its own folder
with index.html so URLs are clean (/site-cuts-melbourne/, etc.).

Idempotent: running again overwrites all pages. Keep this script in-repo
for future suburb expansions or copy edits.

Usage:  python _build_lps.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_URL = "https://www.apolloearthworks.com.au"


def js(s):
    """JSON-encode a string for safe inclusion in JSON-LD blocks."""
    return json.dumps(s, ensure_ascii=False)

# ============================================================
# Per-page config
# Each entry generates one /<slug>/index.html
# ============================================================

# Keys:
#   slug              folder + URL path (no slashes)
#   page_type         "service" or "suburb"  (drives schema selection)
#   keyword           exact-match H1 keyword (e.g. "Site Cuts Melbourne")
#   h1_html           full H1 HTML with brand-light highlight span
#   meta_title        <60 chars
#   meta_desc         <160 chars
#   og_desc           <200 chars (short hook)
#   hero_para         hero subhead, 1-2 sentences
#   hero_image        path under ../Assets/  (use existing webp set)
#   hero_caption      short label under hero image
#   hero_chip         tiny badge text top of image
#   service_cards     list of (title, body) tuples - 6 cards
#   process_steps     list of 4 (title, body) tuples
#   gallery           list of 3 (alt, caption, file) tuples (files in ../Assets/)
#   areas             list of suburbs/areas (used for suburb LP "service area" or
#                     omitted on suburb pages where it's the location itself)
#   areas_intro       paragraph intro to areas section (page-specific framing)
#   faqs              list of 7 (q, a) tuples
#   schema_service    Service schema serviceType + offer-catalog item names
#   testimonial       (text, author, role) tuple - "review pending" if not collected
#   final_cta_para    closing paragraph above the final CTA button
#   service_links     list of 3 (label, slug) tuples for the cross-link block
# ============================================================

SERVICE_PAGES = [
    # C1
    {
        "slug": "site-cuts-melbourne",
        "page_type": "service",
        "keyword": "Site Cuts Melbourne",
        "h1_html": 'Site Cuts Melbourne.<br><span class="text-brand-light">Cut Right. Cut Once.</span>',
        "meta_title": "Site Cuts Melbourne | Apollo Earthworks",
        "meta_desc": "Residential and commercial site cuts across Melbourne. Excavation to slab spec, fixed quotes, ticketed operators, free on-site assessment. Call 0431 560 908.",
        "og_desc": "Melbourne site cut specialists. Excavation to slab spec, fixed quotes, ticketed operators, free quotes.",
        "hero_para": "Site cuts done to engineer's spec, ready for slab pour. We level, batter and remove spoil across Eastern, South East and Mornington Peninsula Melbourne. Most residential cuts wrap in one to three days, with our own tipper fleet handling cartage so the build doesn't sit waiting.",
        "hero_image": "Site-Preparation",
        "hero_caption": "Residential site cut, Eastern suburbs",
        "hero_chip": "Excavator 5T",
        "service_cards": [
            ("Residential Site Cuts", "Single dwellings, dual occupancies, and townhouse sites cut to engineer's spec. Most residential cuts wrap in one to three days, with full tipper haulage included in the quote."),
            ("Commercial Site Cuts", "Larger blocks, multi-unit sites and commercial pads. Up to 30T excavators paired with our tipper fleet for fast spoil removal across multi-week jobs."),
            ("Cut to Slab Level", "Final trim and base prep so concreters can pour straight onto a clean, level pad. We work to surveyor pegs and engineer's drawings - no guesswork."),
            ("Bench Cuts on Sloping Sites", "Stepped or terraced cuts on sloped Melbourne lots. We assess the fall, batter the cut for safety, and leave a stable platform for the next trade."),
            ("Tight-Access Cuts", "1.7T to 5T excavators for tight inner-suburb sites with limited side-access. We protect existing structures and fences while still moving volume."),
            ("Rock + Hard Ground", "Hydraulic rock-breaker attachments for basalt and hard-ground sites. Assessed on site so rock doesn't blow your fixed quote."),
        ],
        "process_steps": [
            ("Send us your plans", "Email engineer's drawings or call with the basics."),
            ("Free site assessment", "We walk the block and confirm scope and access."),
            ("Fixed quote and booking", "Clear price. Locked timeline. Nothing hidden."),
            ("Cut, trim, clean", "Site cut to spec, spoil removed, pad ready for slab."),
        ],
        "gallery": [
            ("Site preparation in Melbourne's east", "Site preparation", "Site-Preparation.webp"),
            ("Base preparation and civil works on a Melbourne site", "Base prep & civil", "base-preparation-civil-works.webp"),
            ("Material export and cartage from a Melbourne site cut", "Cartage & spoil removal", "material-export-cartage.webp"),
        ],
        "areas_intro": "Our yard is in Mount Waverley and we travel daily across the Eastern, South East and Mornington Peninsula suburbs. If your site is within roughly 50km of the CBD, we can be there. Sample of suburbs we regularly cut sites in:",
        "faqs": [
            ("How much does a site cut cost in Melbourne?", "Site cut pricing depends on the volume of material to be removed, site access, soil type, and whether tipping is included. Most residential site cuts fall between $3,000 and $15,000. We provide fixed quotes after a free on-site assessment so there are no surprises."),
            ("How long does a site cut take?", "A standard residential site cut usually takes one to three days from start to finish. Larger blocks, sloping sites, or jobs with rock can take longer. We confirm exact timelines with each quote and commit to the dates we book."),
            ("Do you handle the spoil and cartage?", "Yes. We run our own tandem tipper fleet, so spoil removal is included in the quote. You don't need to coordinate a separate cartage contractor or worry about tip fees blowing out."),
            ("What machines do you use for site cuts?", "We match the machine to the site. Tight inner-suburb cuts run on 1.7T to 5T excavators. Standard residential cuts use 5T to 14T machines. Larger commercial cuts run 20T to 30T excavators paired with our tipper fleet."),
            ("Do you cut sites with rock or hard ground?", "Yes. We carry hydraulic rock-breaker attachments for basalt and hard-ground sites common across parts of Melbourne. We assess for rock during the on-site quote so it's priced into the fixed number, not added later."),
            ("Can you cut on sloping or tight-access sites?", "Yes. We run smaller machines for tight side-access, and we cut bench or stepped pads on sloping blocks. We protect fences, drives, and neighbouring structures throughout."),
            ("How quickly can you start?", "For most residential cuts we can attend site for a quote within 24 to 48 hours and book works within one to two weeks of acceptance. Urgent cuts can often be slotted in sooner. Call 0431 560 908 to check current availability."),
        ],
        "schema_service": {
            "serviceType": "Site Cuts",
            "offers": ["Residential Site Cuts", "Commercial Site Cuts", "Bench Cuts on Sloping Sites", "Tight-Access Site Cuts", "Rock Breaking and Removal"],
        },
        "final_cta_para": "Send us the plans or just the address. Fixed quotes, free site assessments, honest timelines on every site cut across Melbourne.",
        "service_links": [
            ("Material Removal", "material-removal-melbourne"),
            ("Drainage", "drainage-melbourne"),
            ("Land Clearing", "land-clearing-melbourne"),
        ],
    },
    # C2
    {
        "slug": "material-removal-melbourne",
        "page_type": "service",
        "keyword": "Material Removal Melbourne",
        "h1_html": 'Material Removal Melbourne.<br><span class="text-brand-light">Dirt, Rock, Spoil. Gone.</span>',
        "meta_title": "Material Removal Melbourne | Apollo Earthworks",
        "meta_desc": "Dirt, rock and spoil removal across Melbourne. Tipper fleet, fast turnaround, fixed quotes. Builders, owner-builders, civil contractors. Call 0431 560 908.",
        "og_desc": "Melbourne material removal: dirt, rock, spoil. Tipper fleet, fast turnaround, fixed quotes.",
        "hero_para": "Get dirt, rock and excavation spoil off site fast. Our own tandem tipper fleet means we don't wait on third-party cartage - we load, run, and tip on the same day. Service across Eastern, South East and Mornington Peninsula Melbourne for builders, owner-builders, and civil contractors.",
        "hero_image": "material-export-cartage",
        "hero_caption": "Material export, Eastern suburbs",
        "hero_chip": "Tandem Tipper",
        "service_cards": [
            ("Dirt and Soil Removal", "Site cut spoil, excavation arisings, and surplus topsoil hauled off site by our own tippers. Disposed at licensed tips - we handle the paperwork."),
            ("Rock Removal", "Broken rock from basalt sites, rock-breaker arisings, and large stones moved off site quickly. Loaded with excavator buckets, hauled in tandems."),
            ("Excavation Spoil Cartage", "We run our own tippers in convoy with our excavators so spoil leaves the site as fast as it's dug. No double handling, no stockpile blocking access."),
            ("Standalone Cartage", "Already have a stockpile? We can quote standalone cartage with our tipper fleet, no excavation required. Useful for builders cleaning up between trades."),
            ("Clean Fill and Spoil Categorisation", "Clean fill, contaminated, or category C/D - we sort and dispose to the correct tip. Your fixed quote covers the right disposal pathway."),
            ("Fast-Turnaround Removal", "Same-day or next-day cartage available for urgent removal. Call before 7am to check availability for that day's run."),
        ],
        "process_steps": [
            ("Tell us the volume", "Cubic metres, soil type, and access details."),
            ("Free site check (if needed)", "We confirm access for tippers and load point."),
            ("Fixed cartage quote", "Per-load or per-job, including tip fees."),
            ("Load, haul, tip", "Tippers in convoy, paperwork handled, site cleared."),
        ],
        "gallery": [
            ("Material export and cartage on a Melbourne site", "Material export & cartage", "material-export-cartage.webp"),
            ("Drainage and spoil removal cartage in Melbourne", "Spoil removal cartage", "drainage-spoil-removal-cartage.webp"),
            ("Excavator loading tipper on Melbourne site", "Excavator + tipper convoy", "excavation-pools.webp"),
        ],
        "areas_intro": "Tippers run daily out of our Mount Waverley yard across the Eastern, South East and Mornington Peninsula suburbs. If you're inside roughly 50km of the CBD, we can quote and load on short notice.",
        "faqs": [
            ("How much does material removal cost in Melbourne?", "Cartage pricing depends on volume, soil type, distance to the disposal site, and access at the load point. We quote per-load or per-job up front so you know the total before we start. Call 0431 560 908 for a fast quote."),
            ("Do you handle the disposal and tip fees?", "Yes. Tip fees and disposal paperwork are included in our cartage quote. We dispose at licensed tips and sort by clean fill, contaminated, or category C/D as required."),
            ("Can you cart away rock and broken concrete?", "Yes. We cart broken rock from basalt sites, rock-breaker arisings, and concrete demo material. Disposal site varies by material type, all priced into the fixed quote."),
            ("Can you do standalone cartage without excavation?", "Yes. If you already have a stockpile or material from another trade, we can quote tipper cartage on its own. Useful for builders cleaning up between trades or after a manual dig."),
            ("How fast can you start?", "Same-day or next-day cartage is often possible if you call before 7am. Booked-ahead jobs lock in to a confirmed date. Urgent removals get priority slots where available."),
            ("Do you provide a Tip Receipt or weighbridge docket?", "Yes. We provide tip receipts and weighbridge dockets on request, useful for owner-builder records, insurance claims, or council compliance."),
            ("What sizes are your tippers?", "We run tandem tippers suitable for residential and commercial cartage. We can scale up to truck-and-dog combinations for larger jobs - quoted per project."),
        ],
        "schema_service": {
            "serviceType": "Material Removal and Cartage",
            "offers": ["Dirt and Soil Removal", "Rock Removal", "Excavation Spoil Cartage", "Standalone Tipper Cartage", "Clean Fill and Contaminated Spoil Disposal"],
        },
        "final_cta_para": "Cubic metres, access, and where you are - that's all we need to quote. Tipper fleet ready across Melbourne.",
        "service_links": [
            ("Site Cuts", "site-cuts-melbourne"),
            ("Rubbish Removal", "rubbish-removal-melbourne"),
            ("Site Cleans", "site-cleans-melbourne"),
        ],
    },
    # C3
    {
        "slug": "rubbish-removal-melbourne",
        "page_type": "service",
        "keyword": "Rubbish Removal Melbourne",
        "h1_html": 'Site Rubbish Removal Melbourne.<br><span class="text-brand-light">One Call. Site Clear.</span>',
        "meta_title": "Site Rubbish Removal Melbourne | Apollo Earthworks",
        "meta_desc": "Construction site rubbish removal across Melbourne. Bins, end-of-job clears, rubble and demo waste. Tipper fleet, fixed quotes. Call 0431 560 908.",
        "og_desc": "Melbourne site rubbish removal: bins, end-of-job clears, rubble and demo waste. Fixed quotes, fast turnaround.",
        "hero_para": "Construction site rubbish, demolition rubble, and end-of-job clears handled across Eastern, South East and Mornington Peninsula Melbourne. Our excavator + tipper combo loads and hauls in one trip - no waiting on a separate skip company, no back-and-forth.",
        "hero_image": "rubbish-removal",
        "hero_caption": "Site clear, residential build",
        "hero_chip": "Tipper + Excavator",
        "service_cards": [
            ("End-of-Build Site Clears", "Final clean-up before handover. We pick up rubble, off-cuts, packaging and surplus materials so the site is hand-over ready."),
            ("Demolition Rubble Removal", "Brick, tile, concrete and demo arisings loaded out by excavator and tippered to the right tip - sorted clean fill vs mixed waste."),
            ("Builders' Rubbish Removal", "Off-cut timber, plasterboard, packaging and general site rubbish hauled away in one trip. No skip wait, no double handling."),
            ("Garden and Green Waste", "Tree stumps, branches, and green waste from clearing or landscaping prep. Tippered out to green-waste tips."),
            ("Mixed Site Waste", "Whole-site clear-outs after a long job - mixed timber, metal, concrete, soil. We sort what's clean fill from what's mixed waste so you don't pay landfill rates on rubble."),
            ("Storm and Job-Site Cleanup", "After a storm, accident or busy week, we can mobilise quickly to clear the site so the next trade can get in."),
        ],
        "process_steps": [
            ("Tell us what's there", "Rough volume, type of waste, access."),
            ("Quote and book", "Fixed price, locked time slot."),
            ("Load and haul", "Excavator + tipper, in and out fast."),
            ("Tip and tidy", "Disposed correctly, site swept down."),
        ],
        "gallery": [
            ("Construction site rubbish removal in Melbourne", "Site rubbish clear", "rubbish-removal.webp"),
            ("End-of-job site clean in Melbourne", "End-of-job clean", "site-clean.webp"),
            ("Material cartage from Melbourne site", "Rubble cartage", "material-export-cartage.webp"),
        ],
        "areas_intro": "We service Melbourne's east, south east and the Mornington Peninsula daily out of our Mount Waverley yard. Sample suburbs:",
        "faqs": [
            ("How much does site rubbish removal cost?", "Pricing depends on volume, type of waste (clean fill vs mixed vs green), access, and tip distance. Most residential end-of-job clears fall in a $400 to $2,000 range. We give fixed quotes up front - no surprise tip fees."),
            ("Do you sort the waste so I don't pay landfill rates on clean fill?", "Yes. We separate clean fill, rubble, mixed waste, and green waste at the load. Each gets routed to the right tip, so you only pay landfill disposal on what actually goes to landfill."),
            ("How fast can you clear a site?", "Most residential sites are cleared in one visit, often the same day or next day if booked early. Larger commercial clears are scoped during the quote so the timeline is locked in."),
            ("Do you take demolition rubble?", "Yes. Brick, tile, concrete, render, and demolition arisings - all handled. Loaded out by excavator into tippers and disposed at the correct facility."),
            ("Can you handle green waste and stumps?", "Yes. Tree stumps, branches, and green waste from land clearing or landscape prep are tippered out to green-waste tips."),
            ("Do I need to be on site?", "No. Once we have access and a clear scope, we can run the clear without you being there. We send photos before and after if requested."),
            ("Do you provide tip receipts?", "Yes. Available on request - useful for owner-builder records, insurance, or council compliance documentation."),
        ],
        "schema_service": {
            "serviceType": "Site Rubbish and Construction Waste Removal",
            "offers": ["End-of-Build Site Clears", "Demolition Rubble Removal", "Builders' Rubbish Removal", "Green Waste Removal", "Mixed Site Waste Removal"],
        },
        "final_cta_para": "We'll clear it in one trip. Send us a couple of photos and the address - we'll come back with a fixed price.",
        "service_links": [
            ("Site Cleans", "site-cleans-melbourne"),
            ("Material Removal", "material-removal-melbourne"),
            ("Land Clearing", "land-clearing-melbourne"),
        ],
    },
    # C4
    {
        "slug": "site-cleans-melbourne",
        "page_type": "service",
        "keyword": "Site Cleans Melbourne",
        "h1_html": 'Site Cleans Melbourne.<br><span class="text-brand-light">Site-Ready. Hand-Over Ready.</span>',
        "meta_title": "Construction Site Cleans Melbourne | Apollo Earthworks",
        "meta_desc": "Construction site cleans across Melbourne. Between-trade tidies, end-of-build clears, hand-over prep. Excavator + tipper combo, fixed quotes. Call 0431 560 908.",
        "og_desc": "Melbourne construction site cleans. Between-trade tidies, end-of-build clears, hand-over prep. Fixed quotes.",
        "hero_para": "Get the site back to a working state - or hand-over ready - across Eastern, South East and Mornington Peninsula Melbourne. From between-trade tidies to final hand-over cleans, we use the same excavator + tipper combo that runs our earthworks crews, so we move volume fast.",
        "hero_image": "site-clean",
        "hero_caption": "End-of-build clean, residential",
        "hero_chip": "Excavator 3T",
        "service_cards": [
            ("End-of-Build Cleans", "Final clean before client hand-over. Rubbish, off-cuts, surplus materials gone. Site swept and ready for landscaping or occupation."),
            ("Between-Trade Cleans", "Reset the site between trades so the next crew walks onto a working space. Common before slab pour, frame stand-up, or render start."),
            ("Hand-Over Site Prep", "Owner-builders and developers needing a clean, photographable site for hand-over inspections, photography, or sign-off."),
            ("Post-Demolition Cleans", "Post-demo site reset. Rubble, brick, tile and metal cleared so excavation or new build can start clean."),
            ("Whole-Site Spring Clean", "Long-running jobs accumulate mess. We can do a whole-site reset in a single visit so the project runs cleaner from there on."),
            ("Fence and Boundary Tidy", "Off-cuts and rubbish blown into fence lines, neighbours' yards, or street kerbs gathered up and removed."),
        ],
        "process_steps": [
            ("Tell us the scope", "Whole site, single trade clean, or hand-over ready."),
            ("Free site walk (if needed)", "We confirm access and what's leaving."),
            ("Fixed quote", "Price for the clean, including tip fees and cartage."),
            ("Clean and clear", "Excavator + tipper, sweep down, photo confirmation."),
        ],
        "gallery": [
            ("Construction site clean in Melbourne", "Site clean - residential", "site-clean.webp"),
            ("Site rubbish removed in Melbourne", "Rubbish removed", "rubbish-removal.webp"),
            ("Cartage and material export in Melbourne", "Cartage out", "material-export-cartage.webp"),
        ],
        "areas_intro": "Site clean crews run out of our Mount Waverley yard daily. We cover Melbourne's east, south east and the Mornington Peninsula. Sample suburbs:",
        "faqs": [
            ("How much does a construction site clean cost?", "Cleans are priced on volume of waste, access, and how much sweep-down is needed. Most residential end-of-build cleans fall in a $500 to $2,500 range. We quote fixed before starting."),
            ("How long does a site clean take?", "Most residential cleans wrap in half a day to a full day. Larger commercial sites or post-demo cleans can take one to three days, locked in during the quote."),
            ("What's the difference between a site clean and rubbish removal?", "Rubbish removal is purely loading and hauling waste off site. A site clean is broader - it includes rubbish removal plus sweep-down, fence-line tidy, and getting the site visually presentable."),
            ("Do you take the rubbish away or just gather it?", "We take it away. Excavator + tipper combo means we load and haul in the same visit. No skip waiting in the driveway, no separate cartage booking."),
            ("Can you clean a site that's still actively being built?", "Yes. Between-trade cleans are common - we work around scheduled trades and can usually do the clean in a single half-day visit so no one is held up."),
            ("Will you sweep down the slab and surrounding area?", "Yes. End-of-build and hand-over cleans include sweep-down of slab, drive, and immediate surrounds. We don't mop or wash floors - that's a different trade."),
            ("Do you provide before/after photos?", "Yes, on request. Useful for hand-over records, owner-builder documentation, or marketing photos before the next stage."),
        ],
        "schema_service": {
            "serviceType": "Construction Site Cleans",
            "offers": ["End-of-Build Site Cleans", "Between-Trade Cleans", "Hand-Over Site Prep", "Post-Demolition Cleans", "Whole-Site Reset Cleans"],
        },
        "final_cta_para": "Hand-over ready or just back to a working site - we'll clean it in one visit. Call or send a couple of photos for a fixed quote.",
        "service_links": [
            ("Rubbish Removal", "rubbish-removal-melbourne"),
            ("Material Removal", "material-removal-melbourne"),
            ("Land Clearing", "land-clearing-melbourne"),
        ],
    },
    # C5
    {
        "slug": "land-clearing-melbourne",
        "page_type": "service",
        "keyword": "Land Clearing Melbourne",
        "h1_html": 'Land Clearing Melbourne.<br><span class="text-brand-light">Block-Ready in Days.</span>',
        "meta_title": "Land Clearing Melbourne | Apollo Earthworks",
        "meta_desc": "Land clearing across Melbourne. Tree stumps, vegetation, debris and full-block clears for new builds, subdivisions and landscaping. Fixed quotes. Call 0431 560 908.",
        "og_desc": "Melbourne land clearing: stumps, vegetation, debris, full-block clears for new builds and subdivisions.",
        "hero_para": "Get a block ready for the build - cleared, levelled, and hauled away. We handle stumps, vegetation, debris and full-block clears across Eastern, South East and Mornington Peninsula Melbourne for owner-builders, developers and landscapers.",
        "hero_image": "Site-Preparation",
        "hero_caption": "Block prep, Eastern suburbs",
        "hero_chip": "Excavator 8T",
        "service_cards": [
            ("Stump Removal", "Tree stumps removed by excavator with grab attachment. Hole backfilled and tippered material taken off site."),
            ("Vegetation and Scrub Clearing", "Overgrown blocks cleared down to bare ground. Green waste tippered to a green-waste facility."),
            ("Full Block Clears", "Whole-block clears for new builds and subdivisions. Vegetation, debris, old slabs and stumps - one crew, one timeline."),
            ("Debris and Old-Build Material", "Old fence posts, fallen branches, scrap metal, abandoned building material - cleared and disposed at the right tip."),
            ("Site Strip and Rough Level", "After clearing we can strip topsoil and rough-level the block so it's ready for the surveyor or the next trade."),
            ("Subdivision Block Prep", "Multi-lot subdivisions cleared in sequence. We work to the development timeline so blocks are ready as titles drop."),
        ],
        "process_steps": [
            ("Send a few photos", "Block size, what's there, access from the street."),
            ("Free site walk (if needed)", "Walk the block, check for hazards, confirm scope."),
            ("Fixed clearing quote", "Price for the clear, cartage, and disposal."),
            ("Clear, haul, hand back", "Block cleared, debris gone, ready for the next stage."),
        ],
        "gallery": [
            ("Site preparation and clearing in Melbourne", "Block prep", "Site-Preparation.webp"),
            ("Excavation for landscaping in Melbourne", "Landscape excavation", "excavation-landscaping.webp"),
            ("Material export from Melbourne site", "Cartage out", "material-export-cartage.webp"),
        ],
        "areas_intro": "Land clearing crews run out of our Mount Waverley yard across Melbourne's east, south east and the Mornington Peninsula. Sample suburbs:",
        "faqs": [
            ("How much does land clearing cost in Melbourne?", "Land clearing pricing depends on block size, vegetation density, stumps, debris, and access. Most residential block clears fall in a $1,500 to $8,000 range. Larger or subdivision blocks priced per scope. We quote fixed before starting."),
            ("How long does it take to clear a block?", "A standard residential block clear usually takes one to two days. Heavily vegetated or stump-heavy blocks can take three to five days. Subdivisions are scheduled per lot."),
            ("Do you remove tree stumps?", "Yes. Stumps are removed with an excavator and grab attachment. Hole is backfilled and the spoil tippered out. Larger stumps may need a rock breaker - quoted on assessment."),
            ("Do I need a permit to clear vegetation?", "Some councils require permits for clearing certain native vegetation. We don't pull permits but we can flag during the site walk if a permit is likely required so you can check with council before we start."),
            ("Can you do tree removal as well?", "We remove trees we can safely push or pull with the excavator after stump exposure. For tall standing trees that need a climber or chipper, we recommend a dedicated arborist - we'll then handle the stump and debris."),
            ("Can you strip and level the block after clearing?", "Yes. We can strip topsoil and rough-level the block so it's ready for the surveyor or builder. Often combined with the clearing job for one fixed price."),
            ("How fast can you start?", "Most residential clears can be quoted within 24 to 48 hours and booked within one to two weeks. Subdivisions are programmed against the developer's timeline."),
        ],
        "schema_service": {
            "serviceType": "Land Clearing and Site Preparation",
            "offers": ["Stump Removal", "Vegetation Clearing", "Full Block Clears", "Debris Removal", "Site Strip and Rough Level", "Subdivision Block Prep"],
        },
        "final_cta_para": "Cleared, levelled, hauled away - one crew, fixed quote. Send us photos and the address to get started.",
        "service_links": [
            ("Site Cuts", "site-cuts-melbourne"),
            ("Material Removal", "material-removal-melbourne"),
            ("Site Cleans", "site-cleans-melbourne"),
        ],
    },
    # C6
    {
        "slug": "retaining-walls-melbourne",
        "page_type": "service",
        "keyword": "Retaining Walls Melbourne",
        "h1_html": 'Retaining Walls Melbourne.<br><span class="text-brand-light">Built to Hold. Built to Last.</span>',
        "meta_title": "Retaining Walls Melbourne | Apollo Earthworks",
        "meta_desc": "Retaining walls across Melbourne. Concrete sleeper, timber sleeper, besser block. Engineered, drained, built to last. Fixed quotes. Call 0431 560 908.",
        "og_desc": "Melbourne retaining wall builders. Concrete and timber sleeper, besser block. Engineered, drained, fixed quotes.",
        "hero_para": "Retaining walls built to engineer's spec across Eastern, South East and Mornington Peninsula Melbourne. We do concrete sleeper, timber sleeper and besser block walls - excavated, drained and built so they hold for the long term, not just the photo.",
        "hero_image": "base-preparation-civil-works",
        "hero_caption": "Retaining wall base prep",
        "hero_chip": "Excavator 5T",
        "service_cards": [
            ("Concrete Sleeper Walls", "Galvanised steel posts in concrete footings with concrete sleeper infill. Most popular for residential retaining - clean look, decades of service life."),
            ("Timber Sleeper Walls", "Treated hardwood sleepers with steel post or timber post construction. Suits landscaped gardens and budget-conscious residential projects."),
            ("Besser Block Walls", "Reinforced besser block walls for taller or load-bearing situations. Engineered, drained, capped to the agreed finish."),
            ("Engineered Walls Over 1m", "Walls over 1m typically need an engineer's design. We work directly to engineer drawings and can coordinate the engineer if needed."),
            ("Drainage Behind Walls", "Agi drain, scoria backfill, and weep holes installed correctly so hydrostatic pressure doesn't push the wall over in five years."),
            ("Excavation and Backfill", "We do the full job - excavation for footings, posts in, sleepers/blocks installed, backfill and compaction. One crew, one timeline."),
        ],
        "process_steps": [
            ("Send photos and rough length", "Length of wall, height, what it's holding back."),
            ("Free site assessment", "We measure, check soil and access, confirm material."),
            ("Fixed quote and timeline", "Price including excavation, materials, drainage, backfill."),
            ("Build, drain, finish", "Excavate, post in, fill, drain, backfill - done."),
        ],
        "gallery": [
            ("Base preparation for retaining wall in Melbourne", "Retaining wall base prep", "base-preparation-civil-works.webp"),
            ("Excavation for landscaping in Melbourne", "Wall excavation", "excavation-landscaping.webp"),
            ("Drainage solutions installed in Melbourne", "Drainage behind wall", "drainage-solutions.webp"),
        ],
        "areas_intro": "Retaining wall crews run out of our Mount Waverley yard across the Eastern, South East and Mornington Peninsula suburbs. Sample suburbs:",
        "faqs": [
            ("How much do retaining walls cost in Melbourne?", "Retaining wall pricing depends on length, height, material (concrete sleeper, timber, besser block), drainage requirements, and site access. Most residential walls fall in a $250 to $700 per square metre range, fully built. We quote fixed after a free site assessment."),
            ("Do I need a permit for a retaining wall?", "Walls over 1m typically need a building permit and an engineer's design. We can flag during the site assessment if your planned wall needs council approval, so you can engage a draftsperson or engineer before we start."),
            ("Concrete sleeper vs timber sleeper - which is better?", "Concrete sleepers last decades, look cleaner, and resist termites and rot - a strong default for residential. Timber sleepers cost less up front, suit garden-style landscaping, but need replacement after 15 to 25 years depending on conditions. We can quote both."),
            ("How tall can a retaining wall go?", "Concrete sleeper systems typically go to around 1.2 to 1.5m residential without engineering escalation. Higher walls need an engineer's design and may step up to besser block or reinforced concrete construction."),
            ("Do you install drainage behind the wall?", "Yes. Agi drain, scoria backfill and weep holes are installed correctly behind every wall we build. This is the most common reason cheaply-built walls fail in the first five years - hydrostatic pressure with no drainage."),
            ("Can you work around existing landscaping?", "Yes. We use smaller machines for tight access and protect existing trees, paths, and structures. We'll flag any high-risk root zones during the site assessment."),
            ("How long does a retaining wall take to build?", "A standard 10-20m residential wall usually wraps in two to four days including excavation, footings, posts, infill, drainage and backfill. Larger walls or wet-weather delays can extend - we lock the timeline at quote stage."),
        ],
        "schema_service": {
            "serviceType": "Retaining Wall Construction",
            "offers": ["Concrete Sleeper Retaining Walls", "Timber Sleeper Retaining Walls", "Besser Block Retaining Walls", "Engineered Retaining Walls", "Wall Drainage Installation"],
        },
        "final_cta_para": "Built to engineer's spec, drained correctly, designed to last. Send us photos and the rough length for a fixed quote.",
        "service_links": [
            ("Drainage", "drainage-melbourne"),
            ("Site Cuts", "site-cuts-melbourne"),
            ("Material Removal", "material-removal-melbourne"),
        ],
    },
    # C7
    {
        "slug": "drainage-melbourne",
        "page_type": "service",
        "keyword": "Drainage Melbourne",
        "h1_html": 'Drainage Melbourne.<br><span class="text-brand-light">Move Water. The Right Way.</span>',
        "meta_title": "Drainage Solutions Melbourne | Apollo Earthworks",
        "meta_desc": "Drainage installation across Melbourne. Stormwater, agi drains, sub-soil, surface drainage. Trenched, plumbed, backfilled, compacted. Call 0431 560 908.",
        "og_desc": "Melbourne drainage solutions: stormwater, agi, sub-soil, surface drainage. Trenched, plumbed, backfilled.",
        "hero_para": "Stormwater, agi drains, sub-soil and surface drainage installed across Eastern, South East and Mornington Peninsula Melbourne. We trench, plumb, backfill and compact - leaving the site working how it should and ready for landscape or build to continue.",
        "hero_image": "drainage-solutions",
        "hero_caption": "Drainage trenching, residential",
        "hero_chip": "Excavator 3T",
        "service_cards": [
            ("Stormwater Drainage", "PVC stormwater lines from downpipes, pits, and surface drains to legal discharge points. Cut, plumbed, backfilled, compacted."),
            ("Agi Drains and Sub-Soil", "Slotted ag pipe with scoria/aggregate behind retaining walls, around slabs, and along boundaries to handle ground water."),
            ("Surface Drainage", "Strip drains, channel drains, and grated pits across drives, courtyards and slabs to keep surface water moving."),
            ("Spoon Drains and Swales", "Open or shallow drains where pipework isn't viable - graded so water finds the discharge point under gravity."),
            ("Drainage for Retaining Walls", "Agi drain + scoria + weep holes installed correctly behind every wall. The fix that keeps walls standing for decades."),
            ("Connection to Council Mains", "We can dig and connect into council stormwater pits and laterals - working to council requirements for the discharge."),
        ],
        "process_steps": [
            ("Send the plumbing or site plan", "Plans, photos, or a site walk - whatever you have."),
            ("Free site assessment", "Confirm fall, discharge point, and trench routes."),
            ("Fixed quote and booking", "Price including pipework, fittings, backfill and compaction."),
            ("Trench, plumb, backfill", "Trenched, pipework laid, tested, backfilled and compacted."),
        ],
        "gallery": [
            ("Drainage solutions installed in Melbourne", "Drainage installation", "drainage-solutions.webp"),
            ("Drainage and spoil removal cartage in Melbourne", "Drainage trenching + cartage", "drainage-spoil-removal-cartage.webp"),
            ("Base preparation for civil works in Melbourne", "Base prep", "base-preparation-civil-works.webp"),
        ],
        "areas_intro": "Drainage crews run out of our Mount Waverley yard across Melbourne's east, south east and the Mornington Peninsula. Sample suburbs:",
        "faqs": [
            ("How much does drainage cost in Melbourne?", "Drainage pricing depends on length of run, depth, pipework size, fittings, and connection requirements. Most residential drainage runs fall in a $1,500 to $8,000 range. Larger commercial drainage is quoted per scope. We quote fixed after a free site assessment."),
            ("Do you handle the council connection?", "Yes. We can dig and connect into council stormwater pits and laterals, working to the council's requirements for the discharge. If a council inspection is required, we coordinate the timing."),
            ("What's the difference between stormwater, agi, and surface drainage?", "Stormwater is pipework moving water from downpipes and pits to a discharge point. Agi (sub-soil) is slotted pipe in scoria, picking up ground water. Surface drainage (strip drains, channel drains) catches water from drives and slabs. Most jobs use a combination."),
            ("Do you install drainage behind retaining walls?", "Yes. Agi pipe, scoria backfill and weep holes are installed correctly behind every retaining wall we build. We can also retrofit drainage behind existing walls if water issues are showing."),
            ("Can you fix existing drainage that's failing?", "Often yes. Common failures are blocked agi, undersized stormwater, or no fall. We dig, inspect, identify the problem, and quote the fix. Sometimes a partial replacement is enough."),
            ("Do you compact the trench backfill?", "Yes. Backfill is layered and compacted to spec so the trench doesn't subside under driveways, paths or lawns over the next year."),
            ("How fast can you start?", "Most residential drainage jobs are quoted within 24 to 48 hours and booked within one to two weeks. Urgent water-ingress jobs get priority where possible."),
        ],
        "schema_service": {
            "serviceType": "Drainage Installation",
            "offers": ["Stormwater Drainage", "Agi Drains and Sub-Soil Drainage", "Surface Drainage", "Spoon Drains and Swales", "Retaining Wall Drainage", "Council Stormwater Connection"],
        },
        "final_cta_para": "Trenched, plumbed, backfilled, compacted - left working how it should. Send us your plumbing plan or photos to get a fixed quote.",
        "service_links": [
            ("Retaining Walls", "retaining-walls-melbourne"),
            ("Site Cuts", "site-cuts-melbourne"),
            ("Material Removal", "material-removal-melbourne"),
        ],
    },
]

# C8 - Suburb LPs (umbrella "earthworks-{suburb}" pages)
SUBURB_PAGES = [
    {
        "slug": "earthworks-mount-waverley",
        "suburb": "Mount Waverley",
        "region": "Eastern Melbourne",
        "drive_note": "Our yard is in Mount Waverley itself - we're on local sites every week and operate as a true local earthworks contractor for Mount Waverley and the immediate Monash council area.",
    },
    {
        "slug": "earthworks-mornington",
        "suburb": "Mornington",
        "region": "Mornington Peninsula",
        "drive_note": "Mornington is roughly an hour from our Mount Waverley yard. We service the township and the wider Mornington Peninsula with full earthworks crews, including site cuts, drainage and material cartage.",
    },
    {
        "slug": "earthworks-frankston",
        "suburb": "Frankston",
        "region": "South East Melbourne",
        "drive_note": "Frankston sits about 45 minutes south of our Mount Waverley yard. We work across Frankston, Frankston South, Carrum Downs and Seaford regularly for residential builders and owner-builders.",
    },
    {
        "slug": "earthworks-cranbourne",
        "suburb": "Cranbourne",
        "region": "South East Melbourne",
        "drive_note": "Cranbourne and the surrounding growth corridor is core territory for us. We service Cranbourne, Cranbourne East, Cranbourne West, Clyde and Clyde North - a lot of new-build site cuts and subdivision prep.",
    },
    {
        "slug": "earthworks-berwick",
        "suburb": "Berwick",
        "region": "South East Melbourne",
        "drive_note": "Berwick is around 35 minutes from our Mount Waverley yard. We work Berwick, Beaconsfield, Officer and Pakenham regularly for residential builders, developers and owner-builders in the south east growth corridor.",
    },
]

# ============================================================
# Template
# ============================================================

def build_faq_schema(faqs):
    items = []
    for q, a in faqs:
        items.append(f'''      {{
        "@type": "Question",
        "name": {js(q)},
        "acceptedAnswer": {{ "@type": "Answer", "text": {js(a)} }}
      }}''')
    return ",\n".join(items)


def build_offer_catalog(offers):
    items = []
    for o in offers:
        items.append(f'            {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": {js(o)} }}}}')
    return ",\n".join(items)


def build_service_cards(cards):
    out = []
    for title, body in cards:
        out.append(f'''          <div class="svc-card rounded-xl p-4 sm:p-5 border-l-2 border-l-brand-darker hover:bg-surface-warm">
            <h3 class="font-display font-semibold text-base sm:text-lg mb-1">{title}</h3>
            <p class="text-ink-muted text-sm">{body}</p>
          </div>''')
    return "\n".join(out)


def build_process_steps(steps):
    out = []
    for i, (title, body) in enumerate(steps, start=1):
        out.append(f'''          <div class="relative process-step">
            <div class="step-circle">{i:02d}</div>
            <h3 class="font-display font-semibold text-base mb-1">{title}</h3>
            <p class="text-ink-muted text-xs sm:text-sm">{body}</p>
          </div>''')
    return "\n".join(out)


def build_gallery(items):
    out = []
    for alt, caption, fname in items:
        out.append(f'''          <figure class="relative rounded-xl overflow-hidden shadow-elevated aspect-[4/3] img-overlay">
            <img src="../Assets/{fname}" alt="{alt}" width="800" height="600" class="w-full h-full object-cover" loading="lazy" decoding="async">
            <figcaption class="absolute left-4 bottom-3 z-10 text-white text-xs sm:text-sm font-medium">{caption}</figcaption>
          </figure>''')
    return "\n".join(out)


def build_faqs(faqs):
    out = []
    for q, a in faqs:
        out.append(f'''          <details>
            <summary class="flex items-center justify-between gap-6 py-6">
              <span class="font-display font-semibold text-base sm:text-lg">{q}</span>
              <span class="faq-icon text-brand-darker text-2xl leading-none">+</span>
            </summary>
            <p class="pb-6 text-ink-muted">{a}</p>
          </details>''')
    return "\n".join(out)


def build_areas_grid(areas):
    return "\n".join(f"          <p>{s}</p>" for s in areas)


def build_service_links(links):
    out = []
    for label, slug in links:
        out.append(f'''          <a href="../{slug}/" class="block bg-white rounded-xl p-5 border border-ink/10 hover:border-brand-darker shadow-elevated">
            <p class="font-display font-semibold text-base sm:text-lg text-ink mb-1">{label} Melbourne</p>
            <p class="text-ink-muted text-sm">See pricing, process and FAQs &rarr;</p>
          </a>''')
    return "\n".join(out)


# Standard suburb list used on most service LPs (grouped roughly N -> S)
DEFAULT_AREAS = [
    "Mount Waverley", "Glen Waverley", "Box Hill", "Doncaster",
    "Blackburn", "Ringwood", "Croydon", "Lilydale",
    "Mitcham", "Vermont", "Forest Hill", "Burwood",
    "Camberwell", "Hawthorn", "Kew", "Balwyn",
    "Clayton", "Oakleigh", "Mulgrave", "Springvale",
    "Dandenong", "Noble Park", "Keysborough", "Berwick",
    "Narre Warren", "Cranbourne", "Pakenham", "Officer",
    "Frankston", "Carrum Downs", "Seaford", "Mornington",
    "Mount Eliza", "Mount Martha", "Rosebud", "Sorrento",
]


def build_page(cfg, last_mod="2026-05-15"):
    """Render a single LP HTML string from a service-page config."""
    keyword = cfg["keyword"]
    slug = cfg["slug"]
    canonical = f"{BASE_URL}/{slug}/"
    hero_image = cfg["hero_image"]
    areas = cfg.get("areas", DEFAULT_AREAS)
    testimonial_html = '''<div class="bg-white rounded-2xl p-6 sm:p-8 shadow-elevated max-w-2xl mx-auto border-l-4 border-brand-darker">
          <p class="text-ink text-base sm:text-lg" style="line-height: 1.7;">
            <em>Reviews coming soon. Apollo Earthworks is collecting verified reviews from current Melbourne customers - if you've worked with us, we'd love to hear from you.</em>
          </p>
          <p class="text-ink-muted text-sm mt-4">- Customer reviews in collection</p>
        </div>'''

    # Schema
    service_schema = f'''      {{
        "@type": "Service",
        "serviceType": {js(cfg["schema_service"]["serviceType"])},
        "name": {js(keyword)},
        "provider": {{ "@id": "{BASE_URL}/#business" }},
        "areaServed": [
          {{ "@type": "City", "name": "Eastern Melbourne" }},
          {{ "@type": "City", "name": "South East Melbourne" }},
          {{ "@type": "Place", "name": "Mornington Peninsula" }}
        ],
        "hasOfferCatalog": {{
          "@type": "OfferCatalog",
          "name": "{cfg["schema_service"]["serviceType"]} Services",
          "itemListElement": [
{build_offer_catalog(cfg["schema_service"]["offers"])}
          ]
        }}
      }}'''

    breadcrumb_schema = f'''      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE_URL}/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Services", "item": "{BASE_URL}/services.html" }},
          {{ "@type": "ListItem", "position": 3, "name": {js(keyword)}, "item": {js(canonical)} }}
        ]
      }}'''

    faq_schema = f'''      {{
        "@type": "FAQPage",
        "mainEntity": [
{build_faq_schema(cfg["faqs"])}
        ]
      }}'''

    business_schema = f'''      {{
        "@type": "LocalBusiness",
        "@id": "{BASE_URL}/#business",
        "name": "Apollo Earthworks",
        "image": "{BASE_URL}/Assets/Logo.png",
        "logo": "{BASE_URL}/Assets/Logo.png",
        "telephone": "+61431560908",
        "email": "info@apolloearthworks.com.au",
        "url": "{BASE_URL}/",
        "priceRange": "$$",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "Mount Waverley",
          "addressRegion": "VIC",
          "postalCode": "3149",
          "addressCountry": "AU"
        }},
        "areaServed": [
          {{ "@type": "City", "name": "Eastern Melbourne" }},
          {{ "@type": "City", "name": "South East Melbourne" }},
          {{ "@type": "Place", "name": "Mornington Peninsula" }}
        ],
        "openingHoursSpecification": [{{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
          "opens": "06:00",
          "closes": "19:00"
        }}],
        "sameAs": ["https://www.instagram.com/apolloearthworks"]
      }}'''

    schema_block = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
{business_schema},
{service_schema},
{faq_schema},
{breadcrumb_schema}
    ]
  }}
  </script>'''

    return f'''<!DOCTYPE html>
<html lang="en-AU" style="scroll-behavior:smooth;">
<head>
  <!-- Google tag (gtag.js) - GA4 G-N5M5KC06C5 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-N5M5KC06C5"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-N5M5KC06C5');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- LCP image preload -->
  <link rel="preload" as="image" href="../Assets/{hero_image}-sm.webp" fetchpriority="high" type="image/webp" media="(max-width: 639px)">
  <link rel="preload" as="image" href="../Assets/{hero_image}.webp" fetchpriority="high" type="image/webp" media="(min-width: 640px)">

  <title>{cfg["meta_title"]}</title>
  <link rel="dns-prefetch" href="https://www.googletagmanager.com">
  <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
  <link rel="apple-touch-icon" href="../Assets/Logo-optimized.png">
  <link rel="icon" href="../Assets/Logo-optimized.png">

  <meta name="description" content="{cfg["meta_desc"]}">
  <meta name="robots" content="index, follow">
  <meta name="geo.region" content="AU-VIC">
  <meta name="geo.placename" content="Melbourne">
  <link rel="canonical" href="{canonical}">

  <meta property="og:title" content="{cfg["meta_title"]}">
  <meta property="og:description" content="{cfg["og_desc"]}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_AU">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE_URL}/Assets/Site%20Preparation.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{cfg["meta_title"]}">
  <meta name="twitter:description" content="{cfg["og_desc"]}">

{schema_block}

  <link rel="stylesheet" href="../styles.css">
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: #0A0A0A; line-height: 1.7; }}
    h1, h2, h3, h4, .font-display {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-weight: 700; letter-spacing: -0.02em; line-height: 1.15; }}
    h1 {{ letter-spacing: -0.03em; }}

    .grain::before {{ content: ''; position: absolute; inset: 0; opacity: 0.04; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); pointer-events: none; z-index: 1; }}
    .shadow-elevated {{ box-shadow: 0 1px 2px rgba(10,10,10,0.04), 0 4px 12px rgba(10,10,10,0.06), 0 16px 32px rgba(10,10,10,0.04); }}
    .shadow-floating {{ box-shadow: 0 2px 4px rgba(10,10,10,0.06), 0 8px 24px rgba(10,10,10,0.08), 0 32px 64px rgba(10,10,10,0.08); }}
    .shadow-cta {{ box-shadow: 0 4px 12px rgba(10,10,10,0.12), 0 12px 32px rgba(10,10,10,0.08); }}
    .btn:focus-visible {{ outline: 3px solid #1B8FD1; outline-offset: 3px; }}
    .hero-bg {{ background: #0A0A0A; }}
    .img-overlay::after {{ content: ''; position: absolute; inset: 0; background: linear-gradient(to top, rgba(10,10,10,0.6) 0%, rgba(10,10,10,0.1) 50%); pointer-events: none; }}
    .trust-pill-accent {{ border-top: 2px solid rgba(27,143,209,0.4); }}

    .svc-card {{ position: relative; background: #fff; border: 1px solid rgba(10,10,10,0.06); transition: background-color 0.15s ease; }}
    .svc-card.border-l-2 {{ border-left-width: 2px; }}
    .svc-card.border-l-brand-darker {{ border-left-color: #0E5A85; }}
    .svc-card:hover {{ background-color: #F3F1EC; }}

    .step-circle {{ display: inline-flex; align-items: center; justify-content: center; width: 2.75rem; height: 2.75rem; border-radius: 9999px; background: rgba(27,143,209,0.1); color: #0E5A85; font-weight: 700; font-size: 0.875rem; letter-spacing: 0.02em; margin-bottom: 0.75rem; }}
    .process-step {{ position: relative; }}
    @media (min-width:1024px) {{ .process-step:not(:last-child)::after {{ content: ''; position: absolute; top: 1.375rem; left: calc(2.75rem + 0.75rem); right: -1rem; height: 2px; background: rgba(27,143,209,0.15); }} }}

    .faq details {{ border-bottom: 1px solid rgba(10,10,10,0.08); }}
    .faq details[open] summary .faq-icon {{ transform: rotate(45deg); }}
    .faq summary {{ cursor: pointer; list-style: none; }}
    .faq summary::-webkit-details-marker {{ display: none; }}

    .quote-form-card {{ background: #fff; border-radius: 1rem; padding: 1.75rem; border-top: 3px solid #0E5A85; box-shadow: 0 1px 2px rgba(10,10,10,0.04), 0 4px 12px rgba(10,10,10,0.06); }}
    @media (min-width:640px) {{ .quote-form-card {{ padding: 2.25rem; }} }}
    .quote-input {{ display: block; width: 100%; padding: 0.75rem 1rem; font-size: 0.875rem; line-height: 1.5; color: #0A0A0A; background: #FAFAF8; border: 1px solid rgba(10,10,10,0.12); border-radius: 0.5rem; transition: border-color 0.15s ease, background-color 0.15s ease; }}
    .quote-input:focus {{ outline: none; border-color: #0E5A85; background: #fff; }}
    .quote-input::placeholder {{ color: #9ca3af; }}

    .mobile-call-bar {{ box-shadow: 0 -4px 16px rgba(10,10,10,0.12); }}
    @media (max-width: 640px) {{ body {{ padding-bottom: 72px; }} }}
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            ink: {{ DEFAULT: '#0A0A0A', muted: '#6B6B6B' }},
            brand: {{ DEFAULT: '#1B8FD1', light: '#2BA0E0', darker: '#0E5A85', deep: '#0B4768' }},
            surface: {{ DEFAULT: '#FAFAF8', warm: '#F3F1EC' }}
          }},
          fontFamily: {{ display: ['-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Helvetica','Arial','sans-serif'] }}
        }}
      }}
    }}
  </script>
  <!-- Sutera lead events (GA4) -->
  <script>/* SUTERA_LEAD_EVENTS */
  (function(){{
    function ev(n, p){{ if (typeof window.gtag === 'function') {{ window.gtag('event', n, Object.assign({{transport_type:'beacon'}}, p||{{}})); }} }}
    document.addEventListener('click', function(e){{
      var a = e.target.closest ? e.target.closest('a[href^="tel:"]') : null;
      if (a) ev('click_to_call', {{ link_url: a.getAttribute('href') }});
    }}, true);
    document.addEventListener('submit', function(e){{
      var f = e.target;
      if (!f || f.tagName !== 'FORM' || f.hasAttribute('data-no-lead')) return;
      var action = f.getAttribute('action') || '';
      var isLead = /formspree/i.test(action) || f.querySelector('input[type="email"], input[type="tel"], textarea');
      if (isLead) ev('generate_lead', {{ form_id: f.id || f.getAttribute('name') || 'contact' }});
    }}, true);
  }})();
  </script>
</head>
<body class="bg-surface antialiased overflow-x-hidden">

  <!-- Minimal Landing Nav: logo + phone only -->
  <header id="site-header" class="sticky top-0 z-50 bg-ink/95 backdrop-blur border-b border-white/5" style="transition: transform 0.3s ease;">
    <div class="max-w-6xl mx-auto px-5 sm:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="../" class="flex items-center gap-3" aria-label="Apollo Earthworks">
        <img src="../Assets/Logo-optimized.png" alt="Apollo Earthworks logo" width="160" height="44" class="h-9 sm:h-11 w-auto" decoding="async">
        <span class="hidden sm:block text-white font-display font-semibold text-lg tracking-tight">Apollo Earthworks</span>
      </a>
      <div class="flex items-center gap-2 sm:gap-4">
        <a href="tel:+61431560908" data-conversion="call" class="hidden sm:inline-flex items-center text-white/90 hover:text-white font-medium text-sm">0431 560 908</a>
        <a href="#quick-quote" class="btn inline-flex items-center bg-brand-darker hover:bg-brand text-white font-semibold text-sm px-4 sm:px-5 py-2.5 rounded-full shadow-cta">Get A Free Quote</a>
      </div>
    </div>
  </header>

  <main id="top">

    <!-- HERO -->
    <section class="relative hero-bg grain overflow-hidden">
      <div class="relative z-10 max-w-6xl mx-auto px-5 sm:px-8 pt-14 sm:pt-20 lg:pt-24 pb-16 sm:pb-24 lg:pb-28">
        <div class="grid lg:grid-cols-12 gap-10 lg:gap-14 items-center">
          <div class="lg:col-span-7 text-white">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-xs sm:text-sm text-white/80 mb-6">
              <span class="w-2 h-2 rounded-full bg-brand-light"></span>
              Now booking - limited availability this month
            </div>
            <h1 class="font-display font-bold text-4xl sm:text-5xl lg:text-6xl xl:text-7xl mb-5">
              {cfg["h1_html"]}
            </h1>
            <p class="text-base sm:text-lg lg:text-xl text-white/75 max-w-xl mb-8">
              {cfg["hero_para"]}
            </p>
            <div class="flex flex-col sm:flex-row gap-3 sm:gap-4 mb-8">
              <a href="#quick-quote" class="btn inline-flex items-center justify-center bg-brand-darker hover:bg-brand text-white font-semibold px-6 py-4 rounded-full shadow-cta text-base">Get A Free Site Quote</a>
              <a href="tel:+61431560908" data-conversion="call" class="btn inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/15 border border-white/20 text-white font-semibold px-6 py-4 rounded-full text-base">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h2.28a1 1 0 01.95.68l1.5 4.5a1 1 0 01-.27 1.06L7.91 10.91a12.05 12.05 0 005.18 5.18l1.67-1.55a1 1 0 011.06-.27l4.5 1.5a1 1 0 01.68.95V19a2 2 0 01-2 2h-1C9.72 21 3 14.28 3 6V5z"/></svg>
                Call 0431 560 908
              </a>
            </div>
            <div class="flex flex-wrap gap-x-6 gap-y-3 text-sm text-white/70">
              <span class="inline-flex items-center gap-2"><svg class="w-4 h-4 text-brand-light" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>Fully Insured</span>
              <span class="inline-flex items-center gap-2"><svg class="w-4 h-4 text-brand-light" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>Ticketed Operators</span>
              <span class="inline-flex items-center gap-2"><svg class="w-4 h-4 text-brand-light" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>Fixed Quotes</span>
              <span class="inline-flex items-center gap-2"><svg class="w-4 h-4 text-brand-light" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>Free On-Site Assessment</span>
            </div>
          </div>
          <div class="lg:col-span-5">
            <div class="relative rounded-2xl overflow-hidden shadow-floating border border-white/10 img-overlay">
              <picture>
                <img src="../Assets/{hero_image}.webp" alt="Apollo Earthworks {keyword.lower()} job" width="800" height="1200" class="w-full h-[380px] sm:h-[460px] lg:h-[520px] object-cover" loading="eager" fetchpriority="high" decoding="async">
              </picture>
              <div class="absolute left-5 right-5 bottom-5 z-10 flex items-center justify-between gap-3">
                <div class="text-white">
                  <p class="text-xs uppercase tracking-widest text-brand-light font-semibold">Live job</p>
                  <p class="font-display font-semibold text-lg">{cfg["hero_caption"]}</p>
                </div>
                <div class="bg-white/10 backdrop-blur border border-white/20 rounded-full px-3 py-1.5 text-white text-xs font-medium">{cfg["hero_chip"]}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- TRUST BAR -->
    <section class="bg-ink border-y border-white/5">
      <div class="max-w-6xl mx-auto px-5 sm:px-8 py-6">
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-6 text-center text-white/80">
          <div><p class="font-display font-bold text-2xl text-white">1.7T - 30T</p><p class="text-xs uppercase tracking-wider text-white/70 mt-1">Excavator Fleet</p></div>
          <div><p class="font-display font-bold text-2xl text-white">24-48 hr</p><p class="text-xs uppercase tracking-wider text-white/70 mt-1">Quote Turnaround</p></div>
          <div><p class="font-display font-bold text-2xl text-white">100%</p><p class="text-xs uppercase tracking-wider text-white/70 mt-1">Insured &amp; Compliant</p></div>
          <div><p class="font-display font-bold text-2xl text-white">Fixed Quotes</p><p class="text-xs uppercase tracking-wider text-white/70 mt-1">No Hidden Costs</p></div>
        </div>
      </div>
    </section>

    <!-- QUICK QUOTE FORM -->
    <section id="quick-quote" class="py-10 sm:py-14 bg-surface-warm">
      <div class="max-w-2xl mx-auto px-5 sm:px-8">
        <div class="text-center mb-8">
          <h2 class="font-display font-bold text-2xl sm:text-3xl">Get your free quote within 24-48 hours.</h2>
          <p class="text-ink-muted mt-2">Tell us where and what. We'll call you back with a fixed price.</p>
        </div>
        <form action="https://formspree.io/f/mwvavkwk" method="POST" class="quote-form-card" data-track-gclid>
          <input type="hidden" name="_next" value="https://www.apolloearthworks.com.au/thank-you">
          <input type="hidden" name="_source" value="{slug}">
          <input type="hidden" name="gclid" value="">
          <input type="hidden" name="landing_url" value="">
          <input type="hidden" name="referrer" value="">
          <div class="space-y-4">
            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label for="quick-name" class="block text-sm font-semibold mb-1.5">Name <span class="text-brand-darker">*</span></label>
                <input id="quick-name" name="name" type="text" required autocomplete="name" placeholder="Your name" class="quote-input">
              </div>
              <div>
                <label for="quick-phone" class="block text-sm font-semibold mb-1.5">Phone <span class="text-brand-darker">*</span></label>
                <input id="quick-phone" name="phone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="04XX XXX XXX" class="quote-input">
              </div>
            </div>
            <div>
              <label for="quick-suburb" class="block text-sm font-semibold mb-1.5">Site suburb <span class="text-brand-darker">*</span></label>
              <input id="quick-suburb" name="suburb" type="text" required placeholder="e.g. Ringwood" class="quote-input">
            </div>
            <div>
              <label for="quick-job" class="block text-sm font-semibold mb-1.5">What do you need done? <span class="font-normal text-ink-muted">(optional)</span></label>
              <textarea id="quick-job" name="message" rows="3" placeholder="e.g. {keyword.lower()} for a new build" class="quote-input resize-none"></textarea>
            </div>
          </div>
          <button type="submit" class="btn mt-6 w-full inline-flex items-center justify-center bg-brand-darker hover:bg-brand text-white font-bold px-8 py-4 rounded-full shadow-cta text-base">Request My Free Quote</button>
          <p class="text-xs text-ink-muted mt-3 text-center">Free, no-obligation quote. Your details stay private.</p>
        </form>
      </div>
    </section>

    <!-- SERVICES (this page's specialisation) -->
    <section id="services" class="pt-14 sm:pt-20 pb-20 sm:pb-28 bg-surface">
      <div class="max-w-6xl mx-auto px-5 sm:px-8">
        <div class="max-w-2xl mb-10">
          <p class="text-brand-darker font-semibold text-sm uppercase tracking-widest mb-3">What We Do</p>
          <h2 class="font-display font-bold text-3xl sm:text-4xl lg:text-5xl mb-4">{keyword} - what's covered.</h2>
          <p class="text-ink-muted text-base">As a full-service Melbourne earthworks contractor, we take {keyword.lower().replace(" melbourne", "")} jobs from initial site walk through to a clean, finished hand-over. Every job quoted fixed, every operator ticketed, every site left clean.</p>
        </div>
        <div class="grid grid-cols-2 lg:grid-cols-3 gap-3 sm:gap-4">
{build_service_cards(cfg["service_cards"])}
        </div>
      </div>
    </section>

    <!-- WHY APOLLO -->
    <section class="py-10 sm:py-14 bg-ink text-white">
      <div class="max-w-6xl mx-auto px-5 sm:px-8">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
          <div>
            <h2 class="font-display font-bold text-2xl sm:text-3xl mb-2">Tough work. <span class="text-brand-light">Done right.</span></h2>
            <p class="text-white/70 text-sm sm:text-base">Melbourne builders call Apollo back because jobs run on time, sites are left clean, and quotes don't blow out.</p>
          </div>
          <div class="flex flex-col sm:flex-row items-start sm:items-center gap-3 shrink-0">
            <a href="#quick-quote" class="btn inline-flex items-center justify-center bg-brand-darker hover:bg-brand text-white font-semibold px-6 py-3 rounded-full shadow-cta text-sm w-full sm:w-auto">Get a Fixed Quote</a>
            <a href="tel:+61431560908" data-conversion="call" class="btn inline-flex items-center justify-center gap-2 text-white/80 hover:text-white font-medium px-5 py-3 rounded-full text-sm w-full sm:w-auto">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h2.28a1 1 0 01.95.68l1.5 4.5a1 1 0 01-.27 1.06L7.91 10.91a12.05 12.05 0 005.18 5.18l1.67-1.55a1 1 0 011.06-.27l4.5 1.5a1 1 0 01.68.95V19a2 2 0 01-2 2h-1C9.72 21 3 14.28 3 6V5z"/></svg>
              <span class="sm:hidden">Call Now</span><span class="hidden sm:inline">Call 0431 560 908</span>
            </a>
          </div>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4 mt-10">
          <div class="text-center p-4 rounded-xl bg-white/[0.04] border border-white/10 trust-pill-accent"><p class="font-semibold text-sm">On time</p><p class="text-white/60 text-xs mt-1">No ghosting, no drift</p></div>
          <div class="text-center p-4 rounded-xl bg-white/[0.04] border border-white/10 trust-pill-accent"><p class="font-semibold text-sm">Modern fleet</p><p class="text-white/60 text-xs mt-1">1.7T - 30T excavators</p></div>
          <div class="text-center p-4 rounded-xl bg-white/[0.04] border border-white/10"><p class="font-semibold text-sm">Ticketed ops</p><p class="text-white/60 text-xs mt-1">White Card certified</p></div>
          <div class="text-center p-4 rounded-xl bg-white/[0.04] border border-white/10"><p class="font-semibold text-sm">Fixed quotes</p><p class="text-white/60 text-xs mt-1">No day-rate blowouts</p></div>
          <div class="text-center p-4 rounded-xl bg-white/[0.04] border border-white/10"><p class="font-semibold text-sm">Fully insured</p><p class="text-white/60 text-xs mt-1">SWMS on request</p></div>
          <div class="text-center p-4 rounded-xl bg-white/[0.04] border border-white/10"><p class="font-semibold text-sm">Any scale</p><p class="text-white/60 text-xs mt-1">Residential to civil</p></div>
        </div>
      </div>
    </section>

    <!-- PROCESS -->
    <section class="py-10 sm:py-14 bg-surface-warm">
      <div class="max-w-6xl mx-auto px-5 sm:px-8">
        <p class="text-brand-darker font-semibold text-sm uppercase tracking-widest mb-8">How It Works</p>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 process-grid">
{build_process_steps(cfg["process_steps"])}
        </div>
        <div class="text-center mt-10">
          <a href="#quick-quote" class="btn inline-flex items-center justify-center bg-brand-darker hover:bg-brand text-white font-semibold px-6 py-3 rounded-full shadow-cta text-sm">Get Your Free Quote</a>
        </div>
      </div>
    </section>

    <!-- GALLERY -->
    <section id="gallery" class="py-10 sm:py-14 bg-surface">
      <div class="max-w-6xl mx-auto px-5 sm:px-8">
        <div class="flex items-end justify-between mb-6 gap-4">
          <p class="text-brand-darker font-semibold text-sm uppercase tracking-widest">Recent Work</p>
          <a href="#quick-quote" class="btn inline-flex items-center text-brand-darker hover:text-brand-deep font-semibold text-sm">Quote your project</a>
        </div>
        <div class="grid grid-cols-3 gap-3 sm:gap-4">
{build_gallery(cfg["gallery"])}
        </div>
      </div>
    </section>

    <!-- TESTIMONIAL SLOT -->
    <section class="py-14 sm:py-20 bg-surface-warm">
      <div class="max-w-6xl mx-auto px-5 sm:px-8 text-center">
        <p class="text-brand-darker font-semibold text-sm uppercase tracking-widest mb-3">What Customers Say</p>
        <h2 class="font-display font-bold text-3xl sm:text-4xl mb-8">Built on word of mouth.</h2>
        {testimonial_html}
      </div>
    </section>

    <!-- AREAS -->
    <section id="areas" class="py-14 sm:py-20 bg-surface border-y border-ink/10">
      <div class="max-w-6xl mx-auto px-5 sm:px-8">
        <div class="max-w-3xl mb-8">
          <p class="text-brand-darker font-semibold text-sm uppercase tracking-widest mb-3">Areas We Serve</p>
          <h2 class="font-display font-bold text-3xl sm:text-4xl mb-4">{keyword} across Melbourne's east and south east.</h2>
          <p class="text-ink-muted text-base">{cfg["areas_intro"]}</p>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-x-6 gap-y-1 text-sm text-ink">
{build_areas_grid(areas)}
        </div>
      </div>
    </section>

    <!-- RELATED SERVICES CROSS-LINKS -->
    <section class="py-14 sm:py-20 bg-surface-warm">
      <div class="max-w-6xl mx-auto px-5 sm:px-8">
        <p class="text-brand-darker font-semibold text-sm uppercase tracking-widest mb-3">Related Services</p>
        <h2 class="font-display font-bold text-2xl sm:text-3xl mb-8">Other Melbourne earthworks services we offer.</h2>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
{build_service_links(cfg["service_links"])}
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq" class="py-20 sm:py-28 bg-surface">
      <div class="max-w-3xl mx-auto px-5 sm:px-8">
        <div class="text-center mb-12">
          <p class="text-brand-darker font-semibold text-sm uppercase tracking-widest mb-3">Questions</p>
          <h2 class="font-display font-bold text-3xl sm:text-4xl lg:text-5xl">Frequently asked.</h2>
        </div>
        <div class="faq bg-white rounded-2xl px-6 sm:px-8 shadow-elevated">
{build_faqs(cfg["faqs"])}
        </div>
      </div>
    </section>

    <!-- FINAL CTA -->
    <section class="py-20 sm:py-28 bg-surface-warm">
      <div class="max-w-4xl mx-auto px-5 sm:px-8 text-center">
        <h2 class="font-display font-bold text-3xl sm:text-4xl lg:text-5xl mb-4">Ready to dig in?</h2>
        <p class="text-ink-muted text-base mb-6 max-w-2xl mx-auto">{cfg["final_cta_para"]}</p>
        <div class="flex flex-col sm:flex-row justify-center gap-3">
          <a href="#quick-quote" class="btn inline-flex items-center justify-center bg-brand-darker hover:bg-brand text-white font-semibold px-8 py-4 rounded-full shadow-cta">Get A Free Quote</a>
          <a href="tel:+61431560908" data-conversion="call" class="btn inline-flex items-center justify-center gap-2 text-ink hover:text-brand-darker font-medium px-8 py-4 rounded-full text-base">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h2.28a1 1 0 01.95.68l1.5 4.5a1 1 0 01-.27 1.06L7.91 10.91a12.05 12.05 0 005.18 5.18l1.67-1.55a1 1 0 011.06-.27l4.5 1.5a1 1 0 01.68.95V19a2 2 0 01-2 2h-1C9.72 21 3 14.28 3 6V5z"/></svg>
            Call 0431 560 908
          </a>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="bg-ink text-white/70 py-10">
    <div class="max-w-6xl mx-auto px-5 sm:px-8">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 text-sm">
        <div class="flex items-center gap-3">
          <img src="../Assets/Logo-optimized.png" alt="" width="140" height="32" class="h-8 w-auto opacity-90" loading="lazy" decoding="async">
          <span class="font-display font-semibold text-white">Apollo Earthworks</span>
        </div>
        <div class="flex items-center gap-4 text-xs">
          <a href="../" class="hover:text-white">Home</a>
          <a href="../services.html" class="hover:text-white">Services</a>
          <a href="../contact.html" class="hover:text-white">Contact</a>
          <a href="../privacy.html" class="hover:text-white">Privacy</a>
        </div>
      </div>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-2 sm:gap-x-5 text-xs sm:text-sm mt-6">
        <span>ABN 26 886 956 778</span>
        <span class="hidden sm:inline text-white/30">|</span>
        <span>Mount Waverley VIC 3149</span>
        <span class="hidden sm:inline text-white/30">|</span>
        <a href="mailto:info@apolloearthworks.com.au" class="hover:text-white">info@apolloearthworks.com.au</a>
        <span class="hidden sm:inline text-white/30">|</span>
        <a href="tel:+61431560908" data-conversion="call" class="hover:text-white">0431 560 908</a>
      </div>
      <p class="text-center text-white/60 text-xs mt-4">&copy; <span id="year"></span> Apollo Earthworks. Tough work. Done right.</p>
    </div>
  </footer>

  <!-- Mobile sticky call bar -->
  <div class="sm:hidden fixed bottom-0 left-0 right-0 z-40 bg-ink mobile-call-bar border-t border-white/10">
    <div class="grid grid-cols-2 divide-x divide-white/10">
      <a href="tel:+61431560908" data-conversion="call" class="flex items-center justify-center gap-2 py-4 text-white font-semibold text-sm">
        <svg class="w-4 h-4 text-brand-light" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h2.28a1 1 0 01.95.68l1.5 4.5a1 1 0 01-.27 1.06L7.91 10.91a12.05 12.05 0 005.18 5.18l1.67-1.55a1 1 0 011.06-.27l4.5 1.5a1 1 0 01.68.95V19a2 2 0 01-2 2h-1C9.72 21 3 14.28 3 6V5z"/></svg>
        Call
      </a>
      <a href="#quick-quote" class="flex items-center justify-center gap-2 py-4 bg-brand-darker text-white font-semibold text-sm">Get Free Quote</a>
    </div>
  </div>

  <script>
    document.getElementById('year').textContent = new Date().getFullYear();
    (function() {{
      var header = document.getElementById('site-header');
      var lastScrollY = 0;
      var ticking = false;
      function onScroll() {{
        var currentScrollY = window.scrollY;
        if (currentScrollY > lastScrollY && currentScrollY > 80) {{ header.style.transform = 'translateY(-100%)'; }}
        else {{ header.style.transform = 'translateY(0)'; }}
        lastScrollY = currentScrollY;
        ticking = false;
      }}
      window.addEventListener('scroll', function() {{
        if (!ticking) {{ requestAnimationFrame(onScroll); ticking = true; }}
      }}, {{ passive: true }});
    }})();
    (function() {{
      function getParam(name) {{ var m = window.location.search.match(new RegExp('[?&]' + name + '=([^&]+)')); return m ? decodeURIComponent(m[1]) : ''; }}
      function getCookieGclid() {{ var m = document.cookie.match(/(?:^|;\\s*)_gcl_aw=([^;]+)/); if (!m) return ''; var parts = decodeURIComponent(m[1]).split('.'); return parts.length >= 3 ? parts.slice(2).join('.') : ''; }}
      var gclid = getParam('gclid');
      if (gclid) {{ try {{ sessionStorage.setItem('ga_gclid', gclid); }} catch(e) {{}} }}
      else {{ try {{ gclid = sessionStorage.getItem('ga_gclid') || ''; }} catch(e) {{}} if (!gclid) gclid = getCookieGclid(); }}
      var landingUrl = window.location.href;
      var referrer = document.referrer || '';
      document.querySelectorAll('form[data-track-gclid]').forEach(function(form) {{
        var g = form.querySelector('input[name="gclid"]');
        var l = form.querySelector('input[name="landing_url"]');
        var r = form.querySelector('input[name="referrer"]');
        if (g) g.value = gclid;
        if (l) l.value = landingUrl;
        if (r) r.value = referrer;
        form.addEventListener('submit', function() {{ if (g) g.value = gclid || getCookieGclid(); }});
      }});
    }})();
  </script>
</body>
</html>
'''


def build_suburb_page(s, last_mod="2026-05-15"):
    """Render a suburb LP from suburb config (umbrella earthworks-{suburb})."""
    suburb = s["suburb"]
    region = s["region"]
    slug = s["slug"]
    keyword = f"Earthworks {suburb}"

    cfg = {
        "slug": slug,
        "page_type": "suburb",
        "keyword": keyword,
        "h1_html": f'Earthworks &amp; Excavation<br>{suburb}.<br><span class="text-brand-light">Done Right.</span>',
        "meta_title": f"Earthworks {suburb} | Apollo Earthworks",
        "meta_desc": f"Earthworks and excavation in {suburb}. Site cuts, drainage, material removal, retaining walls. Fixed quotes, ticketed operators, free site assessment. Call 0431 560 908.",
        "og_desc": f"{suburb} earthworks and excavation. Site cuts, drainage, material removal. Fixed quotes, free assessments.",
        "hero_para": f"Full-service earthworks and excavation in {suburb} and across {region}. Site cuts, drainage, material cartage, retaining walls and demolition - one crew, fixed quotes, ticketed operators. {s['drive_note']}",
        "hero_image": "Site-Preparation",
        "hero_caption": f"Earthworks job, {suburb}",
        "hero_chip": "Excavator 5T",
        "service_cards": [
            ("Site Cuts", f"Residential and commercial site cuts in {suburb}, levelled to engineer's spec, ready for slab pour. One to three days for most residential cuts."),
            ("Bulk Excavation", f"Basements, pools, large-volume digs across {suburb} and {region}. Up to 30T excavators paired with our own tipper fleet."),
            ("Drainage", f"Stormwater, agi drains, and surface drainage installed across {suburb}. Trenched, plumbed, backfilled, compacted."),
            ("Material Removal", f"Dirt, rock and spoil removed off site by our own tippers. Fast turnaround across {suburb} and surrounding suburbs."),
            ("Retaining Walls", f"Concrete sleeper, timber and besser block retaining walls built across {suburb}. Engineered, drained, designed to last."),
            ("Demolition &amp; Land Clearing", f"Demolition, land clearing, stump and vegetation removal across {suburb} - getting blocks ready for the next stage."),
        ],
        "process_steps": [
            ("Call or request a quote", f"Tell us the {suburb} address, the job and the timeline."),
            ("Free site assessment", "We walk the site and confirm scope and access."),
            ("Fixed quote and booking", "Clear price. Locked timeline. Nothing hidden."),
            ("Dig, finish, clean", "On time, to spec, site left clean."),
        ],
        "gallery": [
            ("Site preparation in Melbourne", "Site preparation", "Site-Preparation.webp"),
            ("Drainage solutions in Melbourne", "Drainage", "drainage-solutions.webp"),
            ("Material export and cartage", "Cartage out", "material-export-cartage.webp"),
        ],
        "areas": [suburb] + [a for a in DEFAULT_AREAS if a != suburb],
        "areas_intro": f"We work {suburb} and the surrounding suburbs daily out of our Mount Waverley yard. {s['drive_note']} Sample of suburbs we regularly work in:",
        "faqs": [
            (f"Do you service {suburb}?", f"Yes. {s['drive_note']} Most {suburb} jobs are quoted within 24 to 48 hours of contact."),
            (f"How much does a site cut cost in {suburb}?", f"Site cut pricing in {suburb} depends on volume, access, soil type and tipping. Most residential site cuts fall between $3,000 and $15,000. We provide a fixed quote after a free on-site assessment."),
            (f"Do you charge a travel surcharge for {suburb}?", f"No. Travel to {suburb} is included in the fixed quote. There are no kilometre surcharges or float fees added later."),
            (f"What size excavators do you bring to {suburb}?", "We match the machine to the site. Tight access uses 1.7T to 5T machines, standard residential uses 5T to 14T, larger commercial cuts run 20T to 30T excavators with tipper fleet."),
            ("Are you fully insured?", "Yes. Apollo Earthworks is fully insured, OH&S compliant, and all operators hold current White Card and machine tickets. SWMS documentation is available on request."),
            (f"Can you do drainage and retaining walls in {suburb} as well?", f"Yes. We do drainage (stormwater, agi, surface), retaining walls (concrete sleeper, timber, besser block), demolition, land clearing and material removal across {suburb} - one crew, one quote."),
            (f"How quickly can you start a {suburb} job?", f"For most {suburb} residential jobs we can attend site for a quote within 24 to 48 hours and book works within one to two weeks of acceptance. Urgent jobs can often be slotted in sooner."),
        ],
        "schema_service": {
            "serviceType": f"Earthworks and Excavation in {suburb}",
            "offers": ["Site Cuts", "Bulk Excavation", "Drainage", "Material Removal", "Retaining Walls", "Demolition and Land Clearing"],
        },
        "final_cta_para": f"Call Kosta directly or send us your {suburb} site details. Fixed quotes, free assessments, honest timelines.",
        "service_links": [
            ("Site Cuts", "site-cuts-melbourne"),
            ("Drainage", "drainage-melbourne"),
            ("Retaining Walls", "retaining-walls-melbourne"),
        ],
    }
    return build_page(cfg, last_mod=last_mod)


def main():
    written = []
    for cfg in SERVICE_PAGES:
        out_dir = ROOT / cfg["slug"]
        out_dir.mkdir(exist_ok=True)
        html = build_page(cfg)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        written.append(cfg["slug"])

    for s in SUBURB_PAGES:
        out_dir = ROOT / s["slug"]
        out_dir.mkdir(exist_ok=True)
        html = build_suburb_page(s)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        written.append(s["slug"])

    print(f"Built {len(written)} landing pages:")
    for slug in written:
        print(f"  /{slug}/")


if __name__ == "__main__":
    main()
