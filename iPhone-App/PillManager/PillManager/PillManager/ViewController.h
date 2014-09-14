//
//  ViewController.h
//  PillManager
//
//  Created by ruut on 13.09.14.
//  Copyright (c) 2014 Nico Merzbach. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "APIClient.h"

@interface ViewController : UIViewController <APIClientProtocol>
@property (weak, nonatomic) IBOutlet UILabel *patientName;
@property (weak, nonatomic) IBOutlet UIImageView *patientImage;
@property (weak, nonatomic) IBOutlet UILabel *patientAge;
@property (weak, nonatomic) IBOutlet UILabel *patientKrankenkasse;
- (IBAction)detailsForPatientButton:(id)sender;



@end