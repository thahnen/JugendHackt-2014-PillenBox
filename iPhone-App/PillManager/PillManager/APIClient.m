#import "APIClient.h"
#define BASE_API_URL @"http://api.dsab.try-net.de/api.php"

@interface APIClient()
@property NSString *user;
@property NSString *password;
@end


@implementation APIClient


-(id)init {
    self = [super init];
    if(!self) {
        return nil;
    }
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    NSString *userFromUserDefaults = [defaults objectForKey:@"PILL_BOX_USER"];
    NSString *passwordFromUserDefaults = [defaults objectForKey:@"PILL_BOX_PASSWORD"];
    
    if(userFromUserDefaults && passwordFromUserDefaults) {
        self.user = userFromUserDefaults;
        self.password = passwordFromUserDefaults;
    } else {
        NSLog(@ "APIClient: Couldn't find UserDefaults for user or password!");
        self.user = @"";
        self.password = @"";
    }
    
    return self;
}

-(void)sendRequestWithAction:(id)action {
    AFHTTPRequestOperationManager *manager = [AFHTTPRequestOperationManager manager];
    NSDictionary *parameters = @{@"action": action,
                                 @"data": @"",
                                 @"user": self.user,
                                 @"password": self.password};
    
    [manager POST:BASE_API_URL parameters:parameters success:^(AFHTTPRequestOperation *operation, id requestedObject) {
        
        if ([self.delegate respondsToSelector:@selector(didFinishRequest:withAction:)]) {
            [self.delegate didFinishRequest:requestedObject withAction:@"login"];
        }
        
        [self.delegate didFinishCheckLogin:requestedObject];
    } failure:^(AFHTTPRequestOperation *operation, NSError *error) {
        NSLog(@"AFHTTPRequestOperation Error: %@", error);
        
    }];

}

-(void)checkLogin {
    AFHTTPRequestOperationManager *manager = [AFHTTPRequestOperationManager manager];
    NSDictionary *parameters = @{@"action": @"login",
                                 @"data": @"",
                                 @"user": self.user,
                                 @"password": self.password};
    
    [manager POST:BASE_API_URL parameters:parameters success:^(AFHTTPRequestOperation *operation, id requestedObject) {

        if ([self.delegate respondsToSelector:@selector(didFinishRequest:withAction:)]) {
            [self.delegate didFinishRequest:requestedObject withAction:@"login"];
        }
        
        [self.delegate didFinishCheckLogin:requestedObject];
    } failure:^(AFHTTPRequestOperation *operation, NSError *error) {
        NSLog(@"AFHTTPRequestOperation Error: %@", error);
        
    }];
    
}

-(void)getName {
    AFHTTPRequestOperationManager *manager = [AFHTTPRequestOperationManager manager];
    NSDictionary *parameters = @{@"action": @"getMyName",
                                 @"data": @"",
                                 @"user": self.user,
                                 @"password": self.password};
    
    [manager POST:BASE_API_URL parameters:parameters success:^(AFHTTPRequestOperation *operation, id requestedObject) {
        NSLog(@"Name from API: %@", requestedObject);
        if ([self.delegate respondsToSelector:@selector(didFinishRequest:withAction:)]) {
            [self.delegate didFinishRequest:requestedObject withAction:@"getMyName"];
        }
        [self.delegate didFinishGetName:requestedObject];
    } failure:^(AFHTTPRequestOperation *operation, NSError *error) {
        NSLog(@"AFHTTPRequestOperation Error: %@", error);
        
    }];
}

-(void)getPatientList {
    [self sendRequestWithAction:@"getPatientList"];
    
    
}


@end
