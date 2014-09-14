//
//  PatientListCell.h
//  PillManager
//
//  Created by ruut on 14.09.14.
//  Copyright (c) 2014 Nico Merzbach. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface PatientListCell : UITableViewCell
@property (weak, nonatomic) IBOutlet UIImageView *patientImage;
@property (weak, nonatomic) IBOutlet UILabel *patientName;
@property (weak, nonatomic) IBOutlet UILabel *patientAge;
@property (weak, nonatomic) IBOutlet UILabel *patientKrankenkasse;

@end
