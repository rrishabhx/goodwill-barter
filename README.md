# goodwill-barter
## How to Barter?
1. Create user account {T: User}
    1. Pick categories to follow {T: User, UserFollow}
    
2. User Login
3. Landing page with two options:
    1. Products
    2. Services
    
### Products
1. Show a catalog of top user products (Users with high Karma points)
    - > Have a button to show all products
2. Ability to browse and choose product
    1. Create a chat dialog (could be realtime/non-realtime) for personalised message
    2. Owner of product can check the products associated with Interested user.
    3. Owner can accept or decline barter.
    4. After successful barter:
       1. Both products associated with owner and interested user will be unavailable.
       2. Both users will rate each other based on the product received
       3. Ratings will be converted to Karma Points

3. Ability to check barter requests


### Services
1. Show a catalog of top services from followed categories
2. Ability to choose the service of a particular user
    1. Request will reach the owner of service
    2. Owner can check the services offered by interested user.
    3. Owner can choose to accept or decline barter
    > Will include Barter credits after successful implementation of bare minimum barter.
    4. After successful barter:
       1. Both users will rate each other based on how much they like each other's service
       2. Ratings will be converted to Karma Points
3. Ability to check barter requests


### Routes
- '/': Landing page of application -> Should contain two options: products & services
- '/login', '/logout', '/register': Every webpage's Navbar will contain login/register option
- '/profile': User profile page (web-tier) -> Owners can check all barter requests, there items and services
- '/products': Products home page (app-tier/caching service) -> Should contain an Add to Cart button which will redirect current user to owner's timeline with the selected item. 
   - '/owner_timeline': Timeline of owner -> User can send a message along with the barter request to owner
   
- '/services': Services home page -> User specific feed according to the content subscribed by user. User can select any service to barter which will redirect to owner's timeline
  - '/owner_timeline': Timeline of owner -> User can send a message along with the barter request to owner
    

### DB schema
