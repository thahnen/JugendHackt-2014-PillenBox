//
//  LoginViewController.m
//  DSAB Berlin
//
//  Created by Nico Merzbach on 27.12.13.
//  Copyright (c) 2013 Nico Merzbach. All rights reserved.
//

#import "LoginViewController.h"
#import <AFNetworking.h>


@interface LoginViewController ()
@property UIActivityIndicatorView *activityIndicator;

@end

@implementation LoginViewController

-(void)viewDidLoad {
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    NSString* defaultsuser = [defaults objectForKey:@"PILL_BOX_USER"];
    
    if(defaultsuser != nil) {
        self.user.text = defaultsuser;
        self.passwordField.text = @"********";
    }
}

- (IBAction)deleteLoginData {
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    [defaults setObject:nil forKey:@"PILL_BOX_USER"];
    [defaults setObject:nil forKey:@"PILL_BOX_PASSWORD"];
    [defaults synchronize];
    
    self.user.text = @"";
    self.passwordField.text = @"";
}

- (IBAction)save:(id)sender {
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    [defaults setObject:self.user.text forKey:@"PILL_BOX_USER"];
    if(![self.passwordField.text isEqualToString:@"********"]) {
        [defaults setObject:self.passwordField.text forKey:@"DSAB_API_PASSWORD"];
    }
    
    APIClient *apiClient = [[APIClient alloc] init];
    apiClient.delegate = self;
    [apiClient checkLogin];
    
    self.activityIndicator = [[UIActivityIndicatorView alloc] initWithFrame:CGRectMake(0, 0, 20, 20)];
    self.activityIndicator.color = [UIColor blackColor];
    
    UIBarButtonItem * barButton = [[UIBarButtonItem alloc] initWithCustomView:self.activityIndicator];
    [self.navbar setRightBarButtonItem:barButton];
    [self.activityIndicator startAnimating];
                       
}


- (IBAction)cancel {
    [self dismissViewControllerAnimated:YES completion:nil];
}


-(void)didFinishCheckLogin:(id)responseObject {
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    if([[responseObject objectForKey:@"success"] isEqualToNumber:@1]) {
        [self.activityIndicator stopAnimating];
        [self dismissViewControllerAnimated:YES completion:nil];
    } else {
        [defaults setObject:nil forKey:@"PILL_BOX_USER"];
        [defaults setObject:nil forKey:@"PILL_BOX_PASSWORD"];
        [self.activityIndicator stopAnimating];
        [self.navbar setRightBarButtonItem:self.saveButton];
    }
    
    [defaults synchronize];
    NSLog(@"%@", [responseObject objectForKey:@"success"]);
    

}

@end
