//
//  LoginViewController.h
//  DSAB Berlin
//
//  Created by Nico Merzbach on 27.12.13.
//  Copyright (c) 2013 Nico Merzbach. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "APIClient.h"

@interface LoginViewController : UIViewController <APIClientProtocol>

@property (weak, nonatomic) IBOutlet UITextField *user;
@property (weak, nonatomic) IBOutlet UITextField *passwordField;
@property (strong, nonatomic) IBOutlet UIBarButtonItem *saveButton;
@property (weak, nonatomic) IBOutlet UINavigationItem *navbar;

- (IBAction)save:(id)sender;
- (IBAction)deleteLoginData;


@end

