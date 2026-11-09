Project: Mapestate – Map-Based Real Estate Marketplace
Act as a senior product architect, UI/UX designer, and full-stack mobile application developer.

Build a premium, modern real estate marketplace application for both Android and iOS.
1. Core concept
   The application should be map-first.
When users open the app, the first screen must display an interactive map showing nearby properties using exact geographical pins.

Users should be able to:
- Discover properties near their current location.
- Search properties by city, locality, area, or PIN code.
- View exact property locations on the map.
- Filter properties by sale or rent.
- Switch between map view and list view.
- Tap a property pin to see a property preview.
- Open the full property details.
- Contact the owner, agent, or builder.
  The experience should be similar to Google Maps combined with a premium real estate marketplace.
2. Home screen – Map-first interface
   Make the interactive map the main home screen.
Top section:
- Search bar: "Search location, area or property"
- Current location button.
- Filter button.
- Notification icon.
- Profile icon.
  Below the search bar, add two main tabs:
1. BUY
2. RENT
   Property category filters:
BUY:
- Land / Plot for Sale
- Independent House
- Villa
- Apartment / Flat
- Commercial Property
- Agricultural Land
  RENT:
- Independent House
- Apartment / Flat
- Commercial Shop
- Commercial Office Space
- Warehouse
- Co-working Space
  Display properties on the map using individual location pins.
Each pin should show:
- Property price.
- Property category.
- Small property thumbnail when selected.
  When a user taps a pin, open a bottom information card containing:
- Property image.
- Price.
- Property title.
- Location.
- Land area / built-up area.
- Number of bedrooms, if applicable.
- Owner or agent details.
- View Details button.
  Allow users to drag the map and automatically load properties within the visible map boundaries.
3. Advanced property search
   Provide advanced filters.
Common filters:
- Minimum and maximum price.
- Location.
- Property category.
- Property size.
- Posted date.
- Owner or agent listing.
- Verified properties only.
  BUY filters:
- Plot size in square yards / square feet.
- Facing direction (East, West, North, South).
- Road width.
- HMDA / DTCP / RERA approval.
- Bedrooms.
- Bathrooms.
- Parking.
- Ready to move / Under construction.
  RENT filters:
- Monthly rent.
- Security deposit.
- Furnished / Semi-furnished / Unfurnished.
- Bedrooms.
- Bathrooms.
- Parking.
- Family / Bachelor preference.
- Commercial property type.
4. Property details page
   Every property must have a detailed page containing:
- Multiple high-quality property photos.
- Property video.
- Exact map location.
- Property price.
- Price per square yard or square foot.
- Property description.
- Plot dimensions.
- Facing direction.
- Road width.
- Floor information.
- Amenities.
- Approval and legal document information.
- Owner or agent profile.
- Listing date.
- Similar properties nearby.
  Add action buttons:
- Call Owner.
- WhatsApp Owner.
- Send Enquiry.
- Save to Favorites.
- Share Property.
- Get Directions.
5. User accounts and listing management
   Support three types of users:
6. Property Buyer / Tenant
7. Property Owner
8. Real Estate Agent / Builder
   Authentication:
- Mobile number OTP.
- Email login.
- Google login.
- Apple login.
  Owners and agents should be able to:
- Post new properties.
- Upload multiple photos and videos.
- Select property location by dropping a pin on the map.
- Enter property dimensions and pricing.
- Edit listings.
- Pause or deactivate listings.
- Manage enquiries.
- View listing analytics.
6. Exact location and map functionality
   Map functionality is a critical feature.
Integrate Google Maps or Mapbox.

Requirements:
- GPS-based current location.
- Exact property coordinates (latitude and longitude).
- Manual pin placement.
- Reverse geocoding.
- Search by locality.
- Nearby property discovery.
- Map clustering when many properties are nearby.
- Dynamic property loading based on map movement.
- Directions to property.
- Separate map markers for land, houses, apartments, and commercial properties.
  Do not use approximate random pins. Each published property must have a location selected by the listing owner or agent.
For privacy, allow residential owners to choose whether to show the exact house location or an approximate public location.
7. Additional application sections
Bottom navigation:
1. Explore – Map and property discovery.
2. Favorites – Saved properties.
3. Post Property – Create new listing.
4. Enquiries – Messages and enquiries.
5. Profile – Account and settings.
6. Premium features
   Implement:
- Nearby property alerts.
- Saved search alerts.
- Price drop notifications.
- Recently viewed properties.
- Similar property recommendations.
- Chat between buyers and owners.
- Verified owner and agent badges.
- Report suspicious listings.
- Duplicate listing detection.
- Admin approval workflow.
9. Admin dashboard
   Create a separate web-based admin panel.
Admin should be able to:
- Manage users.
- Verify owners and agents.
- Approve or reject property listings.
- Review reported properties.
- Manage categories.
- Monitor enquiries.
- Manage subscriptions.
- View analytics.
- Identify duplicate and fraudulent listings.
10. Design requirements
    Create a premium, modern, minimal interface.
Design direction:
- Google Maps-inspired map experience.
- Clean white backgrounds.
- Dark navy typography.
- Green or teal accent color.
- Rounded property cards.
- Smooth animations.
- Modern icons.
- Bottom sheet interactions.
- Responsive layouts.
  Prioritize the map experience over traditional property listing grids.
11. Technology stack
    Build using:
Mobile application:
- React Native with Expo.
- TypeScript.
- Android and iOS support.
  Backend:
- Node.js / NestJS.
- PostgreSQL with PostGIS for geospatial queries.
- REST APIs.
  Maps:
- Google Maps SDK or Mapbox.
  Storage:
- AWS S3 for property photos and videos.
  Authentication:
- Firebase Authentication or a secure OTP provider.
  Notifications:
- Firebase Cloud Messaging and Apple Push Notification Service.
  Admin:
- Next.js web dashboard.
  Deployment:
- AWS cloud infrastructure.
12. Important database requirements
    Create database entities for:
- Users.
- Properties.
- Property categories.
- Property images.
- Property videos.
- Property locations.
- Favorites.
- Enquiries.
- Conversations.
- Messages.
- Reviews.
- Verification documents.
- Notifications.
- Subscriptions.
  Use PostgreSQL PostGIS to support efficient nearby-property searches using geographical coordinates and radius-based queries.
13. Development instructions
    Do not build just a static UI prototype.
Build a functional application with:
- Working navigation.
- Interactive maps.
- Functional property search.
- Working filters.
- Property creation.
- Image uploads.
- Authentication.
- Property detail pages.
- Favorites.
- Enquiries.
- Backend APIs.
- Database integration.
  Start by developing the complete map-first home screen with realistic sample property data.
Then implement authentication, property listings, search, filters, property details, and backend integration.

Use reusable components, clean architecture, secure APIs, and production-quality code.

The final product must be ready for future deployment to Google Play Store and Apple App Store.
