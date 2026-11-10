# Mapestate — Product Requirements Document (MVP)

## Problem
Map-first real estate marketplace for Android/iOS where buyers/tenants discover
properties on an interactive map, and owners/agents post listings with exact
pin-drop locations.

## MVP scope (shipped)
- **Map-first home**: Leaflet (via WebView) cross-platform map with property pins
  that display price labels. Tap pin → bottom preview card with photo, price, title,
  area, bedrooms, "View Details".
- **Search + filters**: text search (title/locality/city/pincode), BUY/RENT segment,
  category chips (6 BUY categories, 6 RENT categories), bbox-based auto-load as the
  map moves. Advanced filters modal: price range, bedrooms, verified-only.
- **List / map toggle**.
- **Property details**: gallery, price, verified badge, specs (BHK, area, facing,
  parking, plot size, road width, approval, furnishing), description, amenities,
  inline map, directions button, owner card, similar nearby, sticky action bar
  (Call / WhatsApp / Enquiry).
- **Favorites**: save/unsave from details, list screen.
- **Enquiries**: send from property details; sent/received tabs.
- **Post property**: form with pin-drop on map, multi-image upload via Emergent
  Object Storage, BUY/RENT + category selection.
- **Auth**: email/password (JWT, bcrypt) + Emergent-managed Google OAuth.
  Three roles: buyer, owner, agent.
- **Profile**: avatar, role badge, sign out.
- **Seeded data**: ~88 properties across Hyderabad, Bangalore, Mumbai, Chennai.

## Update (Jun 2026) – Guest browsing
- No login wall: map, listings, filters and property details work for guests.
- Login is requested only for actions: favorite, post property, call/WhatsApp/enquiry.
  Favorites/Post/Enquiries/Profile tabs show a sign-in prompt; after signing in the user returns to where they were.
- Fixes: filters keep BUY/RENT, category, search and view mode (shared filter store);
  PATCH /api/properties validated with a typed model; post form resets and opens the new listing;
  enquiry errors shown; share button works.
- Map tiles: OpenStreetMap (Leaflet). Web preview uses an iframe; native uses WebView.

## Update (Jun 2026) – Owner tools, chat, alerts, admin
- **Approval workflow**: new listings start "In review" (pending), hidden from the public until an admin approves. Rejected listings show the admin note; editing resubmits them.
- **My Listings** (Profile → My Listings): status badge, views, chats, enquiries, saves; Edit, Pause / Reactivate. Owners can choose approximate location.
- **Chat**: "Chat" button on property pages opens a conversation with the owner; Enquiries tab → Chats / Received / Sent with unread badges (polling every 4–8s).
- **Saved searches + alerts**: bookmark button on the map saves BUY/RENT, category, search, filters and visible area; in-app notifications (bell with badge) when a matching listing goes live (sent once per listing).
- **Reports**: "Report this listing" with reasons.
- **Admin panel** (Profile → Admin Panel, admin role only): review queue with possible-duplicate flags, approve/reject; open reports (dismiss / remove listing); verify owners & agents (sets Verified badge on their listings); stats.
- Admin seeded from backend .env (ADMIN_EMAIL / ADMIN_PASSWORD).
- Only live listings accept chats, favorites, enquiries and reports; unavailable listings show a "Listing not available" screen.

## Backlog
- P1: push notifications for alerts/chat (needs deploy + build), OTP / Apple login, video upload, map pin clustering
- P2: price-drop alerts, subscriptions / featured listings, reviews, verification document upload, split server.py into routers

## Tech stack
- Mobile: Expo SDK 58 + TypeScript + expo-router
- Backend: FastAPI + MongoDB (`2dsphere` geospatial index for near/bbox queries)
- Map: Leaflet + CARTO voyager tiles inside WebView (works on web preview and native)
- Storage: Emergent Managed Object Storage
- Auth: JWT (email/password) + Emergent Managed Google OAuth

## Deferred follow-ups
Chat, video upload, price-drop/nearby alerts, admin dashboard, verification workflow,
duplicate detection, reporting, subscriptions, OTP login, Apple login, clustering.
