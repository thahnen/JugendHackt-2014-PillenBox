//
//  PatientListCell.m
//  PillManager
//
//  Created by ruut on 14.09.14.
//  Copyright (c) 2014 Nico Merzbach. All rights reserved.
//

#import "PatientListCell.h"

@implementation PatientListCell

- (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];
    if (self) {
        // Initialization code
    }
    return self;
}

- (void)awakeFromNib
{
    // Initialization code
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated
{
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
